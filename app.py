import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
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

@app.route("/")
@app.route("/get_cafes")
def get_cafes():
    cafes = mongo.db.cafes.find()
    return render_template("cafes.html", cafes=cafes)


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
    if request.method == "POST":
        # check if username exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            # make sure hashed passwords match user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))

            else:
                # passwords do not match
                flash("Sorry! Incorrect Username and/or Password")
                return redirect(url_for("signin"))
            
        else:
            # username doesn't exist in database
            flash("Sorry! Incorrect Username and/or Password")
            return redirect(url_for("signin"))

    return render_template("signin.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # retrieve the session user's username from database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    
    if session["user"]:
        return render_template("profile.html", username=username)
    
    return redirect(url_for("signin"))


@app.route("/signout")
def signout():
    # remove user from session cookies
    flash("You have successfully been signed out")
    session.pop("user")
    return redirect(url_for("signin"))


@app.route("/add_cafe", methods=["GET", "POST"])
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
        mongo.db.cafes.insert_one(cafe)
        flash("Cafe Added Successfully!")
        return redirect(url_for("get_cafes"))

    countries = mongo.db.countries.find().sort("country_name", 1)
    power_options = mongo.db.power_options.find().sort("power_outlets", 1)
    free_wifi_options = mongo.db.free_wifi_options.find().sort("free_wifi", 1)
    wifi_speed_options = mongo.db.wifi_speed_options.find().sort("wifi_speed", 1)
    return render_template(
        "add_cafe.html", countries=countries, power_options=power_options, 
        free_wifi_options=free_wifi_options, wifi_speed_options=wifi_speed_options)


@app.route("/edit_cafe/<cafe_id>", methods=["GET", "POST"])
def edit_cafe(cafe_id):
    if request.method == "POST":
        current_date = datetime.now().strftime("%d/%m/%Y")
        mongo.db.cafes.update_one(
            {"_id": ObjectId(cafe_id)}, {
                '$set': {
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
        cafe_id = ObjectId(cafe_id)
        mongo.db.cafes.update_one({"_id": cafe_id}, {"$set": edit})
        flash("Cafe Updated Successfully!")

    cafe = mongo.db.cafes.find_one({"_id": ObjectId(cafe_id)})
    countries = mongo.db.countries.find().sort("country_name", 1)
    power_options = mongo.db.power_options.find().sort("power_outlets", 1)
    free_wifi_options = mongo.db.free_wifi_options.find().sort("free_wifi", 1)
    wifi_speed_options = mongo.db.wifi_speed_options.find().sort("wifi_speed", 1)
    return render_template(
        "edit_cafe.html", cafe=cafe, countries=countries, power_options=power_options, 
        free_wifi_options=free_wifi_options, wifi_speed_options=wifi_speed_options)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)