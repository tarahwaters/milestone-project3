import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from functools import wraps
from bson.objectid import ObjectId
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Signin required decorator
def signin_required(f):
    @wraps(f)
    def signin_wrap(*args, **kwargs):
        # check if "user" is already in session
        if "user" in session:
            return f(*args, **kwargs)
        # "user" not in session
        else:
            flash("Please sign in to your account first!")
            return redirect(url_for("signin"))

    return signin_wrap

# Admin required decorator
# code credit from https://www.perplexity.ai/ and
# https://flask-admin.readthedocs.io/en/latest/introduction/#securing-admin-views


def admin_required(f):
    @wraps(f)
    def admin_wrap(*args, **kwargs):
        user = mongo.db.users.find_one({'username': 'admin'})
        if user and user['is_admin']:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('signin'))
    return admin_wrap


@app.route("/")
@app.route("/get_cafes")
def get_cafes():
    cafes = list(mongo.db.cafes.find())
    countries = list(mongo.db.countries.find())
    return render_template("cafes.html", cafes=cafes, countries=countries)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    cafes = list(mongo.db.cafes.find({"$text": {"$search": query}}))
    countries = mongo.db.countries.find().sort("country_name", 1)
    return render_template(
                "cafes.html", cafes=cafes, countries=countries, query=query)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/signin", methods={"GET", "POST"})
def signin():
    if "user" not in session:
        # only when there is no session["user"] cookie present
        if request.method == "POST":
            # check if username exists in database
            existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()}
            )

            if existing_user:
                # make sure hashed passwords match user input
                if check_password_hash(
                        existing_user["password"], request.form.get(
                        "password")):
                    session["user"] = request.form.get("username").lower()
                    username = existing_user.get("username")
                    # for admin users
                    if existing_user.get("username") == "admin":
                        # set the admin session variable
                        session["admin"] = True
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
                    else:
                        flash("Welcome, {}".format(
                                request.form.get("username")))
                        return redirect(url_for("profile", username=session["user"]))

                else:
                    # passwords do not match
                    flash("Sorry! Incorrect Username and/or Password")
                    return redirect(url_for("signin"))
            else:
                # username doesn't exist in database
                flash("Sorry! Incorrect Username and/or Password")
                return redirect(url_for("signin"))

        return render_template("signin.html")
    # user already signed in, then direct to user profile
    return redirect(url_for("profile", username=session["user"]))


@app.route("/profile/<username>", methods=["GET", "POST"])
@signin_required
def profile(username):
    if "user" in session:
        session_username = session["user"]
        # retrieve the session user's username from database
        if session_username:
            if session_username == "admin":
                # retrieves all cafes for admin users
                cafes = list(mongo.db.cafes.find())
            else:
                # retrieves only user published cafes for non-admin users
                cafes = list(mongo.db.cafes.find(
                        {"published_by": session_username}))
        # retrieve image data for countries
        countries = list(mongo.db.countries.find())

        return render_template(
            "profile.html", username=session_username,
            cafes=cafes, countries=countries)
    return redirect(url_for("signin"))


@app.route("/signout")
@signin_required
def signout():
    # remove user from session cookies
    flash("You have successfully been signed out")
    session.pop("user")
    return redirect(url_for("signin"))


@app.route("/add_cafe", methods=["GET", "POST"])
@signin_required
def add_cafe():
    if request.method == "POST":
        current_date = datetime.now().strftime("%d/%m/%Y")
        cafe = {
            "cafe_name": request.form.get("cafe_name"),
            "city_name": request.form.get("city_name"),
            "country_name": request.form.get("country_name"),
            "map_link": request.form.get("map_link"),
            "cafe_description": request.form.get("cafe_description"),
            "power_outlets": request.form.get("power_outlets"),
            "free_wifi": request.form.get("free_wifi"),
            "wifi_speed": request.form.get("wifi_speed"),
            "published_by": session["user"],
            "published_on": current_date,
        }
        cafe_is_valid, error_msg = validate_cafe(cafe)

        if cafe_is_valid:
            mongo.db.cafes.insert_one(cafe)
            flash("Cafe Added Successfully!")
            return redirect(url_for("get_cafes"))
        else:
            flash(error_msg)
            return redirect(url_for("add_cafe"))
    countries = mongo.db.countries.find().sort("country_name", 1)
    power_options = mongo.db.power_options.find().sort("power_outlets", 1)
    free_wifi_options = mongo.db.free_wifi_options.find().sort("free_wifi", 1)
    wifi_speed_options = mongo.db.wifi_speed_options.find().sort(
            "wifi_speed", 1)
    return render_template(
            "add_cafe.html", countries=countries, power_options=power_options,
            free_wifi_options=free_wifi_options,
            wifi_speed_options=wifi_speed_options)


@app.route("/edit_cafe/<cafe_id>", methods=["GET", "POST"])
def edit_cafe(cafe_id):
    if request.method == "POST":
        current_date = datetime.now().strftime("%d/%m/%Y")
        if "admin" in session and session["admin"] or (
                session["user"] == mongo.db.cafes.find_one(
                        {"_id": ObjectId(cafe_id)})['published_by']):
            # Edits the cafe for admin user or published owner of the cafe
            mongo.db.cafes.update_one(
                {"_id": ObjectId(cafe_id)}, {
                    '$set': {
                        "cafe_name": request.form.get("cafe_name"),
                        "city_name": request.form.get("city_name"),
                        "country_name": request.form.get("country_name"),
                        "map_link": request.form.get("map_link"),
                        "cafe_description": request.form.get(
                                "cafe_description"),
                        "power_outlets": request.form.get("power_outlets"),
                        "free_wifi": request.form.get("free_wifi"),
                        "wifi_speed": request.form.get("wifi_speed"),
                        "published_by": session["user"],
                        "published_on": current_date,
                    }
                }
            )
            edit = {
                "cafe_name": request.form.get("cafe_name"),
                "city_name": request.form.get("city_name"),
                "country_name": request.form.get("country_name"),
                "map_link": request.form.get("map_link"),
                "cafe_description": request.form.get("cafe_description"),
                "power_outlets": request.form.get("power_outlets"),
                "free_wifi": request.form.get("free_wifi"),
                "wifi_speed": request.form.get("wifi_speed"),
                "published_by": session["user"],
                "published_on": current_date,
            }
            flash("Cafe Updated Successfully!")
            return redirect(url_for("get_cafes"))
        else:
            # When user is not an admin or the published owner of the cafe
            flash("You are not authorized to perform this action")
            return redirect(url_for("get_cafes"))

    cafe = mongo.db.cafes.find_one({"_id": ObjectId(cafe_id)})
    countries = mongo.db.countries.find().sort("country_name", 1)
    power_options = mongo.db.power_options.find().sort("power_outlets", 1)
    free_wifi_options = mongo.db.free_wifi_options.find().sort("free_wifi", 1)
    wifi_speed_options = mongo.db.wifi_speed_options.find().sort(
        "wifi_speed", 1)
    return render_template(
        "edit_cafe.html", cafe=cafe, countries=countries,
        power_options=power_options,
        free_wifi_options=free_wifi_options,
        wifi_speed_options=wifi_speed_options)


@app.route("/delete_cafe/<cafe_id>")
def delete_cafe(cafe_id):
    if "admin" in session and session["admin"] or (
            session["user"] == mongo.db.cafes.find_one(
                    {"_id": ObjectId(cafe_id)})['published_by']):
        # Deletes the cafe for admin user or cafe owner
        mongo.db.cafes.delete_one({"_id": ObjectId(cafe_id)})
        flash("Cafe Deleted Successfully")
        return redirect(url_for("get_cafes"))
    else:
        flash("You are not authorized to perform this action")
        return redirect(url_for("get_cafes"))
    cafe = mongo.db.cafes.find_one({"_id": ObjectId(cafe_id)})
    return render_template("cafes.html", cafe=cafe)


@app.route("/delete_user_cafe/<cafe_id>")
def delete_user_cafe(cafe_id):
    cafe = mongo.db.cafes.find_one({"_id": ObjectId(cafe_id)})
    if "admin" in session and session["admin"] or (
            session["user"] == mongo.db.cafes.find_one(
                {"_id": ObjectId(cafe_id)})['published_by']):
        # Deletes the cafe for admin user or cafe owner via the profile page
        mongo.db.cafes.delete_one({"_id": ObjectId(cafe_id)})
        flash("Cafe Deleted Successfully")
        return redirect(url_for(
            "profile", username=session["user"]))  # Redirect to user's profile
    else:
        flash("You are not authorized to perform this action")
        return redirect(url_for("get_cafes"))


@app.route("/get_countries")
@admin_required
def get_countries():
    countries = list(mongo.db.countries.find().sort("country_name", 1))
    return render_template("countries.html", countries=countries)


@app.route("/add_country", methods=["GET", "POST"])
@admin_required
def add_country():
    if request.method == "POST":
        country = {
            "country_name": request.form.get("country_name"),
            "image_name": request.form.get("image_name")
        }
        mongo.db.countries.insert_one(country)
        flash("New Country Added!")
        return redirect(url_for("get_countries"))
    return render_template("add_country.html")


@app.route("/edit_country/<country_id>", methods=["GET", "POST"])
@admin_required
def edit_country(country_id):
    if request.method == "POST":
        edit = {
            "country_name": request.form.get("country_name"),
            "image_name": request.form.get("image_name")
        }
        mongo.db.countries.update_one(
            {"_id": ObjectId(country_id)}, {
                '$set': {
                    "country_name": request.form.get("country_name"),
                    "image_name": request.form.get("image_name")
                }
            }
        )
        flash("Country Successfully Updated")
        return redirect(url_for("get_countries"))
    country = mongo.db.countries.find_one({"_id": ObjectId(country_id)})
    return render_template("edit_country.html", country=country)


@app.route("/delete_country/<country_id>")
@admin_required
def delete_country(country_id):
    mongo.db.countries.delete_one({"_id": ObjectId(country_id)})
    flash("Country Successfully Deleted")
    return redirect(url_for("get_countries"))

# Credit for code adapted from http://my-milestone-project3.herokuapp.com/,
# more specifically..
# https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/app.py


def validate_cafe(cafe):
    is_valid = True
    error_msg = []
    # validate cafe name
    if len(cafe["cafe_name"]) < 1:
        is_valid = False
        error_msg.append("Cafe name should be at least 1 character long")
    # validate town / city name
    if len(cafe["city_name"]) < 1:
        is_valid = False
        error_msg.append(
                "Town / city name should be at least 1 character long")
    # validate country selection
    if not cafe["country_name"]:
        is_valid = False
        error_msg.append("Country is not selected")
    # validate google map link
    if not cafe["map_link"]:
        is_valid = False
        error_msg.append("Google Map link must be specified")
    # validate cafe_description
    if len(cafe["cafe_description"]) < 10:
        is_valid = False
        error_msg.append(
            "Description should be between 10 and 250 chracters long")
    # validate power outlets
    if not cafe["power_outlets"]:
        is_valid = False
        error_msg.append("Option is not selected")
    # validate free wifi
    if not cafe["free_wifi"]:
        is_valid = False
        error_msg.append("Option is not selected")
    # validate wifi speed
    if not cafe["wifi_speed"]:
        is_valid = False
        error_msg.append("Option is not selected")
    return is_valid, error_msg


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
