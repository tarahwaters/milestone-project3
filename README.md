![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Cafeworks ☕
# - a full stack web application to share cafe recommendations suitable for remote working

------

**Cafeworks** is a web application that allows user to view and recommend their favourite cafes that are suitable for remote working and study.

It can often be difficult to find the right cafe which offers us everything we need for working / studying remotely - e.g. a free and reliable wifi connection, power outlets for charging laptops and devices, comfortable seating, and good quality food and drink options for refueling are also important!

This app aims to provide a platform where users can share their favourite remote working cafes, and hopefully inpire other cafeworking digital nomads who love to travel and explore the world while they work! 

## Showcase

![Am I Responsive?](/documentation/readme/cafeworks-amiresponsive.jpg "Am I Responsive? Website Mockup")

The **Am I Responsive?** link can be found here - [Am I Responsive?](https://ui.dev/amiresponsive?url=https://cafeworks-5f88ec79e78c.herokuapp.com/)

A **deployed link** to the live website can be found here [Cafeworks Live Website](https://cafeworks-5f88ec79e78c.herokuapp.com/)

---

## Table of Contents

---

## UX:
## Strategy
### Target Audience

The target audience of this web application are anyone who is interested in exploring cafe options for remote work or study around the world. By sharing a cafe suggestion, they are helping to build an online community of cafelovers and remote workers. It might be that the user is on holiday or travelling while they work or study, or they are looking to explore new cafes in their neighbourhood.. hopefully this app will provide some great cafe recommendations that will inspire and satisy their needs.

### User Requirements and Expectations

- Simple and intuitive user interface
- Clear presentation of necessary information to invite the user to join
- Secure platform that uses a login system with username and password to access and manage personal posts
- Quick and easy to search through existing posts
- Quick and easy to create an account and start sharing posts with others
- Quick and easy to add, edit or delete posts from the an account
- Design that is visually attractive
- Accessibility
- Features and navigation system works as expected


### User Stories

#### User
As a user I would like:
- to know what the website is about and what service it is providing
- to be able to register for a secure account by creating a login username and password
- to be able to securely log out or delete the account as needed
- to be able to explore posts that have been shared by other users (even without a registered account)
- to be able to filter more relevant posts via a search bar
- to be able to open an individual post to engage with the content on a full screen
- to be able to add a post via their personal account by filling out a form and submitting it to the website database
- to be able to view the newly shared travel post and edit / delete if required
- to be given a warning when deleting a post, and the option to either cancel or continute with the delete action
- to have confirmation that the add / edit / delete of a post action has been successful
- to see the result of posting action as expected on the main page (i.e. the correct information has been added / updated / removed from view)
- to navigate through the website intuitively and easily
- to have each link, button and action on the website work as expected
- to have an enjoyable experience while engaging with the platform

#### Admin user / Site owner
In addition to the general user expectations, as an admin user / site owner I would like:
- to be able to access all cafe posts from the Admin profile page
- to to able to delete cafe posts by any user, not just those published by myself
- to be able to add / edit / delete countries from the available list of locations
- to be able to upload a country image that is successfully displayed in both the form select option and the appropriate cafe post
- to restrict access to Admin user pages such as 'Manage Locations' securely so that non-admin users can only interact with their own posts

---

## Scope
### Trade Offs

Considering the user requirements and expectations, the table below shows the features that should be implemented to make an appealing and functional interactive game for users. Due to time constraints and my current skill level, some of these features are not implemented at this stage.

[X] indicates opportunities that were considered at the planning stage but were deemed not viable/feasible for this project sprint.
Y / N indicates a Yes / No as to whether each opportunity was acheived and implemented at this stage.

| Opportunity                                                         | Importance | Viability / Feasibility | Outcome |
| ------------------------------------------------------------------- | :--------: | :---------------------: | :------:|
| Register a secure account by creating a signin username + password  |     5      |            5            |    Y    |
| Signin page for registered users                                    |     5      |            5            |    Y    |
| Signout option with confirmation of action                          |     5      |            5            |    Y    |
| Add a cafe post by submission of a form with confirmation of action |     5      |            5            |    Y    |
| Confirmation of successful / unsuccessful actions via a flash msg   |     4      |            4            |    Y    |
| Display of all posts to main home page                              |     5      |            5            |    Y    |
| Display of all posts to admin profile (restricted access)           |     5      |            4            |    Y    |
| Display of published user posts on profile page                     |     4      |            4            |    Y    |
| Filter more relevant posts via search bar on home page              |     3      |            5            |    Y    |
| Edit / delete functionality of  published user posts (non-admin)    |     5      |            5            |    Y    |
| Edit / delete functionality of all posts (admin user only)          |     5      |            5            |    Y    |
| Confirmation of delete action via a pop up modal                    |     5      |            4            |    Y    |
| Restricted access for admin user to manage countries and images     |     5      |            5            |    Y    |
| Add / edit functionality for countries and images                   |     5      |            5            |    Y    |
| Custom Error404 page                                                |     3      |            3            |    N    |
| Option to view an individual cafe on a separate page                |     3      |            3            |    N    |
| Option to delete user account and associated posts [X]              |     4      |            3            |    X    |
| Option to upload a country image along with the country name [X]    |     2      |            2            |    X    |

---

## Structure

### Existing Features

#### Logo link to Homepage

- By clicking the logo on page, the user is redirected back to the Homepage. 

![Logo link to Homepage](/documentation/readme/features/logo-link.jpg)

#### Desktop Navbar Dropdown

- Desktop Navbar - contains a dropdown feature (by [Materialize](https://materializecss.com/navbar.html)) for the 'Account' options in order to save space.

![Navbar (desktop version)](/documentation/readme/features/navbar-desktop.jpg)

- This feature is particularly necessary for the Admin user, as more links are available to use, which take up too much space on medium-large screens.

![Navbar Dropdown for Admin user](/documentation/readme/features/navbar-desktop-admin-dropdown.jpg)

![Navbar Dropdown for Admin user](/documentation/readme/features/navbar-desktop-admin-dropdown2.jpg)

- For non-admin users, this dropdown menu looks slightly different - e.g. before a user is logged in, the Account options are restricted to Signin / Register:

![Navbar Dropdown for Admin user](/documentation/readme/features/navbar-desktop-non-admin-dropdown.jpg)

- Currently, only Admin users have access to the 'Manage Locations' page to add a new country to the list of options.

#### Mobile Navbar Menu

- For smaller devices, the navbar opens from a sidebar menu icon:

![Mobile Navbar Menu](/documentation/readme/features/navbar-mobile.jpg)

![Mobile Navbar Menu](/documentation/readme/features/navbar-mobile-menu.jpg)

#### Signin Form with input validation

- Returning users can input their login details (username and password) via the form in order to access their account and add / edit / delete cafes.

![Signin Confirmation](/documentation/readme/features/signin-form.jpg)

- In the case of an incorrect username or password, the following message is displayed and the user is encouraged to try again:

![Signin Confirmation](/documentation/readme/features/signin-incorrect.jpg)

- Upon a successful signin, the user is redirected to their Profile page along with a Welcome message:

![Signin Confirmation](/documentation/readme/features/signin-confirmation.jpg)

#### Registration Form with input validation

- Users are encouraged to register for an account so that they can start adding their cafe recommendations to the website. The registration form consists of a username and password input for secure user authentication.

![Registration Form](/documentation/readme/features/register-form.jpg)

- Helper text helps guides users to create a valid username and password, and a custom error/success message (via [Materialize](https://materializecss.com/text-inputs.html)) displays in a red (error) or green (success) colour. The form can only be submitted successfully when all inputs have been completed and validated. 

- A flash message is shown to the user upon a successful registration attempt. See below for [Register success](#registration-success---welcome-message-and-redirection-to-profile-page).

#### Registration Success - Welcome message and redirection to profile page
    
- Upon a successful registration (ie. the new username and password has been accepted and saved to the database), the user is redirected to their new Profile page with a 'Registration Successful!' message displayed:

![Successful registration and welcome message](/documentation/readme/features/registration-successful.jpg)

Returning users will see a list of 'My Cafes' that they have published on this Profile page. But as a new user with no cafes added yet, this information is displayed as a message on the profile along with a button to 'Add Cafe'.

#### Signout Confirmation

- Users wishing to signout from their account can click the 'Signout' link in the navbar menu at anytime. The user will then receive confirmation that they are no longer signed in, and they will no longer be able to access their Profile until they sign back in.

![Confirmation of Signout](/documentation/readme/features/signout-confirmation.jpg)

#### Add Cafe Button

- Signed in users can add a cafe to the database by clicking on the 'ADD CAFE' button which redirects to the 'Add Cafe' form:

![Add Cafe Button](/documentation/readme/features/add-cafe-button.jpg)

- If the user is not already signed in and they click the Homepage 'ADD CAFE' button, they will be redirected to signin to their account first with a message explaining this:

![Add Cafe Redirect to Signin](/documentation/readme/features/add-cafe-signin-first.jpg)

- The 'ADD CAFE' button can also be accessed via the Profile page (if no cafes have been added yet, see [Registration Success](#registration-success---welcome-message-and-redirection-to-profile-page))

#### Add Cafe Form

- The Add Cafe form consists of a mix of text-input fields and select options to generate an information card for the cafe. Each input is required for the form to be submitted.

![Add Cafe Form](/documentation/readme/features/add-cafe-form.jpg)

- The 'Country Name' select option consists of a dropdown list with associated country images (already saved as static images, but the Admin user can adjust the image filename from the front-end if necessary).

![Country Name Select dropdown list](/documentation/readme/features/country-name-select-options.jpg)

There are other form-select options for the user to complete, e.g. for Power Outlets Available? / Free Wifi? / Wifi Speed: 

![Form Select Options (example)](/documentation/readme/features/form-select-options.jpg)

#### Add Cafe Form Validation

- Before the form data can be submitted and saved to the database, the user must meet the validation requirements. For example, if the user has not completed the 'Cafe Name' input field (or any other field), then the form will display an error message:

![Add Cafe Form Validation](/documentation/readme/features/form-input-validation.jpg)

- Each input field is required before the 'ADD CAFE' button will confirm that the data has been saved and added to the page:

![Add Cafe Success Message](/documentation/readme/features/add-cafe-success.jpg)

#### Cafe Cards on Homepage and Profile

- Once a cafe has been added successfully by the user, the information will be displayed in a Cafe Card on the homepage, and the user's Profile page (for non-admin users, only cafes published by the signed in user will be visible on the Profile). 

- The image cards adapted from [Materialize](https://materializecss.com/cards.html), are interactive and expandable. In their inactive state they display the country image, cafe name, country and city name:

![Inactive Cafe Cards](/documentation/readme/features/cafe-card.jpg)

- The edit / delete buttons are also visible on inactive cafe cards that were published by the user (or all cafe cards for the admin user). See [Edit / Delete buttons](#) for more details of this feature.

- When either the card title (cafe name) / chevron icon / country image are clicked on, the card expands to show the full card of information saved from the cafe form (i.e. Cafe Name / City Name / Country Name etc..):

![Expanded Cafe Card](/documentation/readme/features/cafe-card-expanded.jpg)

- The 'Google Map Link' will open in a separate tab if the URL is working.

- The card can be closed to view the basic info and image view again by either clicking on the X icon or the cafe title.

#### Edit / Delete Cafe buttons

![Edit / Delete buttons](/documentation/readme/features/cafe-card-buttons.jpg)

- The edit / delete cafe buttons on the cafe cards will be visible only for the user who published the cafe (unless the user has admin privileges), either on the homepage or in the 'My Cafes' list of the user's Profile:

![User's Profile Page (e.g. admin)](/documentation/readme/features/profile-page-example.jpg)

- When clicked, these buttons will redirect to either the Edit Cafe form for the cafe, or a delete confirmation modal.




### Future Features

---

## Skeleton

Wireframes for the website were created using the UI wireframe tool, [Balsamiq](https://balsamiq.com/), to plan the layout.

The layout and design were kept consistent across the pages / devices as much as possible.
The overall design evolved as the project was developed, so some of the wireframe designs were not carried out / were adapted.

The app consists of the following pages:
- Home page
- Register and signin page
- Profile page (for users that are signed in)
- Add cafe page
- Edit cafe page
- Delete cafe modal - instead of redirecting to a new page, a modal pop-up was used to confirm the delete action
- Search page

For Admin Users only:
- **Manage locations page**
- **Add country page**
- **Edit country page**

### Wireframes

Below are the initial wireframes created for the project during the planning stage. 
Desktop versions were not created as the layout was intended to be the same as mobile, just on a larger scale (i.e more posts avaialble to view at once on larger devices).
Unfortunately, there was not enough time to implement the Error404 page, but this would be added as part of the next sprint.

#### 1. Wireframes 1

- [Home page / Signin page / Register page](/documentation/readme/wireframes-mob-home-login-register.png "Mobile Version")

#### 2. Wireframes 2

- [Profile page / Individual cafe post](/documentation/readme/wireframes-mob-profile-cafepage.png "Mobile Version")

#### 3. Wireframes 3

- [Add cafe / Edit cafe](/documentation/readme/wireframes-mob-addcafe-editcafe.png "Mobile Version")

#### 4. Wireframes 4

- [Delete cafe / Error404](/documentation/readme/wireframes-mob-delete-error404.png "Mobile Version")


## Surface

### Logo

The cafeworks logo was created using [Canva](https://canva.com/).

![cafeworks logo](/documentation/readme/cafeworks-logo.png "cafeworks logo")

### Color Scheme

[coolors.co](https://coolors.co/) was used to create a color palette for the design.

![cafeworks colorscheme](/documentation/readme/cafeworks-colors.png "cafeworks colorscheme")

As the project evolved and to align more with the Materialize color options, extra colors were used based on the following extended palette:

![cafeworks extended colorscheme](/documentation/readme/cafeworks-extended-color-palette.png "cafeworks colorscheme")

### Typography

[canva.com](https://canva.com/) was used to create a logo from a template and their default font pairing was used from **Canva's 'Ultimate Guide to Font Pairing'**.

"**League Spartan** is a modern typeface with strong structure and geometric form. This contrasts well against the elegant and more traditional style of **Libre Baskerville**. Using a serif for your body copy makes dense information easy to read." - from [Canva Ultimate Guide to Font Pairing](https://www.canva.com/learn/the-ultimate-guide-to-font-pairing/)

- **League Spartan** - for the main title and headings
- **Libre Baskerville** - for descriptive text
- with a backup font of **"Sans serif"**

![Font pairings](/documentation/readme/canva-font-pairing.webp "Font pairings")

## Tools and Technologies Used:

- **HTML5**
- **CSS**
- **Materialize**
- **JavaScript**
- **Python3**

- [GitHub and Github Pages](https://github.com/) - used to securely store the code and to host and deploy the live project
- [GitPod](https://www.gitpod.io/) - used as a cloud-based IDE for development
- [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/) - used for testing and troublshooting code, along with Lighthouse auditing
- [Balsamiq](https://balsamiq.com/wireframes/) - used to create wireframes during project planning
- [Materialize](https://materializecss.com/) - used for front-end components and framework design
- [redketchup.io](https://redketchup.io/) - used for resizing and converting image files to webp format
- [beautifytools](https://beautifytools.com/) - used for beautifying code
- [Coolors](https://coolors.co/) - used to generate a color palette for the website design
- [Canva](https://www.canva.com/) - used to design and edit the card images, gifs and pdf resources used in the game
- [FontJoy](https://fontjoy.com/) - used to generate visually appealing font pairings for  the website
- [JSHint](https://jshint.com/) - used to validate JS code
- [Esprima](https://esprima.org/demo/validate.html) - used to validate JS syntax
- [W3 HTML validator](https://validator.w3.org/nu/) - used to validate HTML
- [W3 Jigsaw](https://jigsaw.w3.org/css-validator/validator) - used to validate CSS
- [Tim Nelson's Markdown Builder](https://traveltimn.github.io/markdown-builder/) to help create the structure and some of the content for the README and TESTING.md files
- [AmIResponsive?](https://ui.dev/amiresponsive?url=https://tarahwaters.github.io/milestone-project2/) - used to create a mockup of the website
- [RandomKeygen](https://randomkeygen.com/) - used to create a secure secret key


## Testing:

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://cafeworks-5f88ec79e78c.herokuapp.com/).

### MongoDB Non-Relational Database

This project uses [MongoDB](https://www.mongodb.com) for the Non-Relational Database.

To obtain your own MongoDB Database URI, sign-up on their site, then follow these steps:

- The name of the database on MongoDB should be called **insert-your-database-name-here**.
- The collection(s) needed for this database should be **insert-your-collection-names-here**.
- Click on the **Cluster** name created for the project.
- Click on the **Connect** button.
- Click **Connect Your Application**.
- Copy the connection string, and replace `password` with your own password (also remove the angle-brackets).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `DATABASE_URL` | user's own value |
| `IP` | 0.0.0.0 |
| `MONGO_DBNAME` | user's own value |
| `MONGO_URI` | user's own value |
| `PORT` | 5000 |
| `SECRET_KEY` | user's own value |

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: python app.py > Procfile`
- *replace **app.py** with the name of your primary Flask app name; the one at the root-level*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
  - `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps, plus a few extras.

The sample `env.py` file should look like the following:

```python
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("MONGO_DBNAME", "user's own value")
os.environ.setdefault("MONGO_URI", "user's own value")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DB_URL", "user's own value")
os.environ.setdefault("DEBUG", "True")
os.environ.setdefault("DEVELOPMENT", "True")
```

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/tarahwaters/milestone-project3)
2. Locate the Code button above the list of files and click it
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git shell or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/tarahwaters/milestone-project3.git`
7. Press Enter to create your local clone.

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/tarahwaters/milestone-project3)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

I have compared both versions extensively and from what I can see, there are no differences between local version and the live site deployed on Heroku.

## Credits

For help with **signin_required decorator**:
- [Python Programming Tutorials](https://pythonprogramming.net/decorator-wrappers-flask-tutorial-login-required/) - Flask Decorators - Login_Required pages Flask Tutorial (code used for **"signin_required" decorator** in app.py)

For help with **admin_required decorator**:
- [Perplexity.AI](https://www.perplexity.ai/) - used to help generate and adapt the code, along with troubleshooting and understanding the methodology

For help with **delete confirmation modals**:
- [Materialize](https://materializecss.com/modals.html#!) - Modal documentation with trigger button (plus js initialization)
- [Dynjashik's MSP3-Movie-collection app](https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/templates/movie.html) - submitted for Code Institute MS3 project ([live link to project](http://my-milestone-project3.herokuapp.com/home)) used as a working reference for the Materialize code

For help with python to **control the visibility of cafes and edit/delete functionality for admin users vs non-admin users**:
- [Perplexity.AI](https://www.perplexity.ai/) and Code Insititute tutor support

For help with **styling the cafe form box drop-shadow**:
- [Josh W Comeau](https://www.joshwcomeau.com/css/designing-shadows/) - adapted CSS code from tutorial

For help with **validation error messages for 'add cafe' form inputs**
- [Dynjashik's MSP3-Movie-collection app](https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/app.py) - submitted for Code Institute MS3 project, validation logic adapted for use

For help with README and TESTING markdown:
- [Markdown Builder](https://traveltimn.github.io/markdown-builder) - README and TESTING tool to help generate the Markdown files and
- [D3lyth](https://github.com/D3lyth/all-i-want-for-christmas/blob/main/README.md) for deployment / cloning instructions


## References 

- **Reference1**: [Link description](#)
- **Reference2**: [Link description](#) - deployed project and [github](#)

- **Reference3**: [Link description](#) - deployed project and [github](#)

- **Reference4**: [Link description](#) - deployed project and [github](#)

- [StackOverflow](https://stackoverflow.com/)
- [MDN Web Docs](https://developer.mozilla.org/en-US/)
- [JavaScript Syntax - W3 Schools](https://www.w3schools.com/js/js_syntax.asp)

For help with **admin authentication**:
- [Flask-Admin Documentation](https://flask-admin.readthedocs.io/en/latest/introduction/#securing-admin-views) - for understanding the different methods available for admin authentication available when using Flask
- [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login) - Admin authentication using Flask-Login

For help with **styling queries**:
- [Google Fonts Manual](https://fonts.google.com/knowledge/using_type/manual_kerning_is_rarely_required) - Adjusting letter spacing for brand logo font
- [Margins](https://www.w3schools.com/cssref/pr_margin.php) - Adjusting margins in CSS

For help with **inserting data to database**:
- [GeeksforGeeks](https://www.geeksforgeeks.org/get-current-date-using-python/) - Getting current date using Python
- [Programiz](https://www.programiz.com/python-programming/datetime/strftime) - Converting 'current date' entry into a string value
- [Python strftime Cheat Sheet](https://strftime.org/)

For help with **updating database functionality**:
- [w3schools](https://www.w3schools.com/python/python_mongodb_update.asp) - Python MongoDB Update method (also debugging help from **Code Insititue Tutor Support**)

For help with **search functionality errors**:
- [StackOverflow](https://stackoverflow.com/questions/16204077/typeerror-object-of-type-cursor-has-no-len) - TypeError: object of type 'Cursor' has no len()
- [MongoDB Manual](https://www.mongodb.com/docs/atlas/atlas-search/tutorial/iterate-cursor-tutorial/) - How to Iterate Your Cursor to View All Results
- **Code Institute Tutor Support** - realising that the python **list()** function was necessary in routing to implement the python **len()** during a search (to check if there are any matching results in the database), otherwise it reverts to **MongoDB Cursor** which caused the TypeError

For help with **displaying country images using jinja looping**:
- [StackOverflow](https://stackoverflow.com/questions/33355159/how-can-i-dynamically-render-images-from-my-images-folder-using-jinja-and-flask) - How can I dynamically render images from my images folder using Jinja and Flask?
- **Code Institute Tutor Support** - for the advice to link the static image filename to the database via "countries.image_name", then support fixing the bugs when using jinja to loop through and display the appropriate country image


## Acknowledgements

- All my friends and family who tested the game and gave me valuable feedback and support along the way
- Code Institute Tutor support
- Cohort Facilitator - [Iris Smok](https://ie.linkedin.com/in/irissmok)
- Mentor for support throughout the project