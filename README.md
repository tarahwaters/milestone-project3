![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# cafeworks ☕
# - a full stack web application to share cafe recommendations suitable for remote working

------

**cafeworks** is a web application that allows user to view and recommend their favourite cafes that are suitable for remote working.

It can often be difficult to find the right cafe which offers us everything we need for working / studying remotely - e.g. a free and reliable wifi connection, power outlets for charging laptops and devices, comfortable seating, and good quality food and drink options for refueling are also important!

This app aims to provide a platform where users can share their favourite remote working cafes, and hopefully inpire other cafeworking digital nomads who love to travel and explore the world while they work! 

## Showcase

![Am I Responsive?](# "Am I Responsive? Website Mockup")

The **Am I Responsive?** link can be found here - [Am I Responsive?](#)

A **deployed link** to the live website can be found here [Website Name](#)

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

---

## Scope
### Trade Offs

Considering the user requirements and expectations, the table below shows the features that should be implemented to make an appealing and functional interactive game for users. Due to time constraints and my current skill level, some of these features are not implemented at this stage.

[X] indicates opportunities that were considered at the planning stage but were deemed not viable/feasible for this project sprint.
Y / N indicates a Yes / No as to whether each opportunity was acheived and implemented at this stage.

| Opportunity                                                      | Importance | Viability / Feasibility | Outcome |
| ---------------------------------------------------------------- | :--------: | :---------------------: | :------:|
| Card-matching memory game that works by user clicking cards      |     5      |            5            |    Y    |
| Timer and move counter that provide up-to-date feedback to user  |     5      |            5            |    Y    |
| HowToPlay modal with set of instructions (with clickable button) |     5      |            5            |    Y    |
| WinMessage modal that pops up when user has completed the game   |     5      |            5            |    Y    |
| Option to restart (with button on main page, also via Win modal) |     5      |            5            |    Y    |
| Access to summary notes page for revision / download afer game   |     3      |            4            |    Y    |
| Option of advanced level / challenge                             |     3      |            2            |    N    |
| Option to adjust audio settings [X]                              |     3      |            2            |    X    |




---

## Structure

### Existing Features

- **Feature 1**

    - Feature description. 

    ![screenshot](#)

- **Feature 2**

    - Feature description.


- **Feature 3**

    - Feature description.

    ![screenshot](#)


### Future Features

- **Future Feature 1**
    - The infocards have already been designed with the potential to include 3 separate details to test learning of specialised cells knowledge (required for the GCSE Biology curriculum) - function / location / features. There could be increased difficulties levels where descriptions contain more complex information, or more cell types could be added as a bonus challenge.

- **Future Feature 2**
    - There could be an option to also add more revision topics to the game so the user can improve their knowledge in other areas of the curriculum.

- **Future Feature 3**
    - Sound effects could be added for when cards are clicked, flipped, matched or not matched. This could be more fun and engaging for the user, and also gives them instant feedback of success or error which may improve learning. This feature could be made optional for when the user prefers a quiet game.

- **Future Feature 4**
    - Details of some issues regarding responsiveness are detailed in the [TESTING.md](TESTING.md) file and these would be worked on in future development. Adding more cell cards as options for the game, could allow the grid layout to be changed (e.g. maximum 3x6 instead of 4x4) to optimise card readability. In future, it may be preferable to also use a responsive grid framework (from Boostrap for example) to avoid some of the issues I faced during styling.

- **Future Feature 5** 
    - Although this was not flagged up as an error during testing, it was considered a warning (and as feedback from user testing). The red/blue colour combination of backfaces for the function cards, may be redesigned for future. Currently, it does not affect readability of the 'Function' name, but may be slightly straining for the eyes. Perhaps an option could be included to toggle between different colour schemes for the game depending on the user's preference or needs.

---

## Skeleton

Wireframes for the website were created using the UI wireframe tool, [Balsamiq](https://balsamiq.com/), to plan the layout across desktop, tablet and mobile devices.

The layout and design was kept consistent across the pages / devices as much as possible.

The main game page consists of:

- A title
- A subtitle description of the game
- A countdown timer is on the top left corner ofthe gamegrid - displays how many seconds are remaining during a game
- A moves counter that is on the top right corner of the gamegrid - displays the number of moves made during a game
- A gamegrid of separated into x2 8 divs displaying the rear side of the cards - two cards can be flipped over at a time to make a match
- A reset button is underneath the gamegrid - gives the user the option to reset the game to the beginning
- A howtoplay button is underneath the gamegrid - gives the user the option to view the game instructions and access the prelearning material
- A footer which contains a copyright statement

### Wireframes

These were the initial wireframes created for the project during the planning stage:

**1. Wireframes 1**

- [Mobile and Table Devices](https://github.com/tarahwaters/milestone-project2/blob/main/documentation/readme/wireframe-mob-gamegrid.png "GameGrid Wireframe for Mobile and Tablet Devices")

- [Desktop Devices](https://github.com/tarahwaters/milestone-project2/blob/main/documentation/readme/wireframe-desktop-gamegrid.png "GameGrid Wireframe for Desktop Devices")

**2. Wireframes 2**

- [Mobile and Table Devices](https://github.com/tarahwaters/milestone-project2/blob/main/documentation/readme/wireframe-mob-howtoplay.png "HowToPlay Modal Wireframe for Mobile and Tablet Devices")

- [Desktop Devices](https://github.com/tarahwaters/milestone-project2/blob/main/documentation/readme/wireframe-desktop-howtoplay.png "HowToPlay Modal Wireframe for Desktop Devices")

**3. Wireframes 3**

- [Mobile and Tablet Devices](https://github.com/tarahwaters/milestone-project2/blob/main/documentation/readme/wireframe-mob-winmessage.png "WinMessage Modal Wireframe for Mobile and Tablet Devices")

- [Desktop Devices](https://github.com/tarahwaters/milestone-project2/blob/main/documentation/readme/wireframe-desktop-winmessage.png "WinMessage Modal Wireframe for Desktop Devices")

## Surface

### Logo

The cafeworks logo was created using [Canva](https://canva.com/).

![cafeworks logo](/documentation/readme/cafeworks-logo.png "cafeworks logo")

### Color Scheme

[coolors.co](https://coolors.co/) was used to create a color palette for the design.

![cafeworks colorscheme](/documentation/readme/cafeworks-colors.png "cafeworks colorscheme")

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
- **Bootstrap**
- **JavaScript**

- [GitHub and Github Pages](https://github.com/) - used to securely store the code and to host and deploy the live project
- [GitPod](https://www.gitpod.io/) - used as a cloud-based IDE for development
- [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/) - used for testing and troublshooting code, along with Lighthouse auditing
- [Balsamiq](https://balsamiq.com/wireframes/) - used to create wireframes during project planning
- Procreate iPad app - used to draw and export the cell images
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
[RandomKeygen](https://randomkeygen.com/) - used to create a secure secret key


## Testing:

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment: **(suitable for MS1 and MS2)**

The site was deployed to GitHub Pages. The steps to deploy are as follows:
- In the [GitHub repository](https://github.com/tarahwaters/milestone-project2), navigate to the Settings tab.
- In the general settings side menu, open **Pages**.
- From the source section drop-down menu, select **Deploy from a branch** and then **Main** Branch, and click "Save".
- The page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment and link to visit the site.

The live link can be found [here](https://tarahwaters.github.io/milestone-project2)

### Local Deployment **(suitable for MS1 and MS2)**

This project can be cloned or forked in order to make a local copy on your own system.

#### Cloning **(suitable for MS1 and MS2)**

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/tarahwaters/milestone-project2) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/tarahwaters/milestone-project2.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/tarahwaters/milestone-project2)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

## Credits

For help with **signin_required decorator**:
- [Python Programming Tutorials](https://pythonprogramming.net/decorator-wrappers-flask-tutorial-login-required/) - Flask Decorators - Login_Required pages Flask Tutorial (code used for **"signin_required" decorator** in app.py)

For help with **admin_required decorator**:
- [Perplexity.AI](https://www.perplexity.ai/) - used to help generate and adapt the code, along with troubleshooting and understanding the methodology

For help with **delete confirmation modals**:
- [Materialize](https://materializecss.com/modals.html#!) - Modal documentation with trigger button (plus js initialization)
- [Dynjashik's MSP3-Movie-collection app](https://github.com/Dynjashik/MSP3-Movie-collection/blob/master/templates/movie.html) - submitted for Code Institute MS3 project ([live link to project](http://my-milestone-project3.herokuapp.com/home)) used as a working reference for the Materialize code

For help with...:
- [Link description](#)
- [Link description](#)
- [Link description](#)


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