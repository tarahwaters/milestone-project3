![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


# TopTenTravel 🌏
# - a full stack web application to share travel recommendations

------

TopTenTravel is a travel sharing web application that allows user to view and post lists of their 'Top Ten' travel experiences around the world. As more users share their favourite places, activities, foods and beverages, and hidden gems from their own personal travel experiences, we can help inspire other potential travellers to have new and enriching experiences of their own. This idea came as a way to share my own itinerary ideas with friends and family who have been interested, but also for myself to learn about others' suggestions whenever I am daydreaming or planning to visit a new destination! This platform offers a simple and easy approach to get quick inpsiration when travel planning, while also being visually appealing and accessible to all users.

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

The target audience of this web application are anyone who is interested in researching or sharing their travel ideas with others. By sharing a post that summarises their 'Top Ten' ideas relating to a travel activity or destination, they are helping to build on the exeperience pool of an online community of like-minded individuals who love travelling and all the world has to offer. Each post includes a succinct summary of users' favourite travel ideas which are easy and quick to access - the aim of the site is to provide interesting and personalised lists for those searching or planning for their dream destination trips.

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
### Color Scheme

[coolors.co](https://coolors.co/) was used to create a color palette for the design.

![Link description](/documentation/readme/colorscheme.png "Link description")

### Typography

[fontjoy.com](https://fontjoy.com/) was used to create aesthetic font pairings for the project.

- **Font1** - for the main title
- **Font2** - for subtitles and headings
- **Font3** - for descriptive text
- with a backup font of **"Sans serif"**

![Font pairings](/documentation/readme/typography.jpg "Font pairings")

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

For help with...:
- [Link description](#)
- [Link description](#)
- [Link description](#)


For help with...:
- [Link description](#)
- [Link description](#)
- [Link description](#)

For help with...:
- [Link description](#)
- [Link description](#)

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

## Acknowledgements

- All my friends and family who tested the game and gave me valuable feedback and support along the way
- Code Institute Tutor support
- Cohort Facilitator - [Iris Smok](https://ie.linkedin.com/in/irissmok)
- Mentor for support throughout the project