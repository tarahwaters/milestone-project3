# Testing

Return back to the [README.md](README.md) file.

The site has been tested manually and using validators/linters to ensure that it is working properly.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Homepage | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcafeworks-5f88ec79e78c.herokuapp.com%2F) | ![screenshot](documentation/testing/validation/validation-html-homepage.jpg) | Section lacks header h2-h6 warning |
| Register Page | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcafeworks-5f88ec79e78c.herokuapp.com%2Fregister) | ![screenshot](documentation/testing/validation/validation-html-register.jpg) | Section lacks header h2-h6 warning |
| Signin Page | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcafeworks-5f88ec79e78c.herokuapp.com%2Fsignin) | ![screenshot](documentation/testing/validation/validation-html-signin.jpg) | Section lacks header h2-h6 warning |
| Profile Page (admin) | n/a | ![screenshot](documentation/testing/validation/validation-html-profile-admin.jpg) | Section lacks header h2-h6 warning |
| Profile Page (non-admin) | n/a | ![screenshot](documentation/testing/validation/validation-html-profile-non-admin.jpg) | Section lacks header h2-h6 warning |
| Manage Locations Page (admin) | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcafeworks-5f88ec79e78c.herokuapp.com%2Fget_countries) | ![screenshot](documentation/testing/validation/validation-html-admin-manage-locations.jpg) | Section lacks header h2-h6 warning |
| Add Cafe Page | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcafeworks-5f88ec79e78c.herokuapp.com%2Fadd_cafe) | ![screenshot](documentation/testing/validation/validation-html-add-cafe.jpg) | Section lacks header h2-h6 warning |
| Edit Cafe Page | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcafeworks-5f88ec79e78c.herokuapp.com%2Fedit_cafe%2F653a41f1bd227e18e6b2d9bd) | ![screenshot](documentation/testing/validation/validation-html-edit-cafe.jpg) | Section lacks header h2-h6 warning |
| Add Country Page (admin) | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcafeworks-5f88ec79e78c.herokuapp.com%2Fadd_country) | ![screenshot](documentation/testing/validation/validation-html-admin-add-country.jpg) | Section lacks header h2-h6 warning |
| Edit Country Page (admin) | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcafeworks-5f88ec79e78c.herokuapp.com%2Fedit_country%2F65a7826ed3bf32d642eed5b6) | ![screenshot](documentation/testing/validation/validation-html-admin-edit-country.jpg) | Section lacks header h2-h6 warning |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files. I have used the live deployed site in the validator.

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcafeworks-5f88ec79e78c.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) | ![screenshot](documentation/testing/validation/validation-css-style.jpg) | Pass: No Errors (Error due to external library only) |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) and [Esprima](https://esprima.org/demo/validate.html) to validate my JS file and check the syntax.

| File | Screenshot | Notes |
| --- | --- | --- |
| script.js | ![screenshot](documentation/testing/validation/validation-js-hint-script.jpg)| Pass: No errors|
| script.js | ![screenshot](documentation/testing/validation/validation-js-esprima-script.jpg)| Pass: No errors|

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| app.py | [PEP8 CI](https://pep8ci.herokuapp.com/) | ![screenshot](documentation/testing/validation/validation-python-app.jpg) | No Errors |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](documentation/testing/browsers/browser-chrome.jpg) | Works as expected |
| Firefox | ![screenshot](documentation/testing/browsers/browser-firefox.jpg) | Works as expected |
| Safari (iPad) | ![screenshot iPad](documentation/testing/browsers/browser-safari.PNG) | Some minor errors such as sticky navbar links (for larger screens), and iOS form select conflict with Materialize settings (see error screenshot below). Otherwise works as expected |
| Safari (mobile) |![screenshot iPhone XS](/documentation/testing/browsers/browser-safari-mobile.JPG) | No errors with the mobile navbar, but the form select issue still persists. Otherwise works as expected |
| Safari (form select error) |![screenshot error iPhone XS](/documentation/testing/browsers/browser-safari-mobile-error.PNG)| Materialize select options are often glitching, but clicking the default iOS <> button can allow the user to still submit the form |
| Brave | ![screenshot](documentation/testing/browsers/browser-brave.jpg) | Works as expected |
| Opera | ![screenshot](documentation/testing/browsers/browser-opera.jpg) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Screenshot | Notes |
| --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/testing/responsiveness/responsive-mobile-devtools.jpg) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/testing/responsiveness/responsive-tablet-devtools.jpg) | Works as expected |
| Laptop (devtools) | ![screenshot](documentation/testing/responsiveness/responsive-17inch-laptop-devtools.jpg) | Works as expected |
| 13inch Laptop | ![screenshot](documentation/testing/responsiveness/responsive-13inch-laptop.jpg) | Works as expected |
| XL Monitor (devtools) | ![screenshot](documentation/testing/responsiveness/responsive-XL-monitor-devtools.jpg) | Minor issues with font-sizing   |
| 4K Monitor (devtools) | ![screenshot](documentation/testing/responsiveness/responsive-4K-monitor-devtools.jpg) | Minor issues with font-sizing |
| iPad Pro | ![screenshot](documentation/testing/responsiveness/responsive-ipad-pro.PNG) | Works as expected ||
| iPhone XS | ![screenshot](documentation/testing/responsiveness/responsive-iphone-XS.JPG) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Homepage | Mobile | ![screenshot](documentation/testing/lighthouse/homepage-mobile.jpg) | Slow load time mainly due to large images and improper image sizing |
| Homepage | Desktop | ![screenshot](documentation/testing/lighthouse/homepage-desktop.jpg) | Slow load time mainly due to large images and improper image sizing |
| Register | Mobile | ![screenshot](documentation/testing/lighthouse/register-mobile.jpg) | Some minor warnings for accessbility due to contrast of background colors, non-sequential heading elements and discernible links/labels |
| Register | Desktop | ![screenshot](documentation/testing/lighthouse/register-desktop.jpg) | Some minor warnings for accessbility due to contrast of background colors, non-sequential heading elements and discernible links/labels |
| Profile (no cafes) | Mobile | ![screenshot](documentation/testing/lighthouse/profile-nocafes-mobile.jpg) | Few accessibility warnings |
| Profile (no cafes) | Desktop | ![screenshot](documentation/testing/lighthouse/profile-nocafes-desktop.jpg) | Few accessibility warnings |
| Profile (all cafes) | Mobile | ![screenshot](documentation/testing/lighthouse/profile-allcafes-mobile.jpg) | Heavy image load time and some accessbility warnings |
| Profile (all cafes) | Desktop | ![screenshot](documentation/testing/lighthouse/profile-allcafes-desktop.jpg) | Heavy image load time and some accessbility warnings |
| Signin | Mobile | ![screenshot](documentation/testing/lighthouse/signin-mobile.jpg) | Few accessibility warnings |
| Signin | Desktop | ![screenshot](documentation/testing/lighthouse/signin-desktop.jpg) | Few accessibility warnings |
| Add Cafe | Mobile | ![screenshot](documentation/testing/lighthouse/add-cafe-mobile.jpg) | Few accessibility warnings |
| Add Cafe | Desktop | ![screenshot](documentation/testing/lighthouse/add-cafe-desktop.jpg) | Few accessibility warnings |
| Edit Cafe | Mobile | ![screenshot](documentation/testing/lighthouse/edit-cafe-mobile.jpg) | Heavy image load time and some accessbility warnings |
| Edit Cafe | Desktop | ![screenshot](documentation/testing/lighthouse/edit-country-desktop.jpg) | Few accessibility warnings |
| Manage Locations (admin) | Mobile | ![screenshot](documentation/testing/lighthouse/manage-locations-mobile.jpg) | Heavy image load time and some accessbility warnings |
| Manage Locations (admin) | Desktop | ![screenshot](documentation/testing/lighthouse/manage-locations-desktop.jpg) | Few accessibility warnings |
| Add Country (admin) | Mobile | ![screenshot](documentation/testing/lighthouse/add-country-mobile.jpg) | Few accessibility warnings |
| Add Country (admin) | Desktop | ![screenshot](documentation/testing/lighthouse/add-country-desktop.jpg) | Few accessibility warnings |
| Edit Country (admin) | Mobile | ![screenshot](documentation/testing/lighthouse/edit-country-mobile.jpg) | Few accessibility warnings |
| Edit Country (admin) | Desktop | ![screenshot](documentation/testing/lighthouse/edit-country-desktop.jpg) | Few accessibility warnings |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| **Homepage** | | | | |
| Logo | Click on Logo | Redirection to Homepage | Pass | |
| Navbar / Sidebar | Click on Home link in navbar | Redirection to Homepage | Pass | |
| | Click on Acccount link in navbar **(user not signed in)** | Opens dropdown account links - Signin / Register | Pass | Only Signin / Register options are available when user is not signed in |
| | Click on Acccount link in navbar **(non-admin user signed in)** | Opens dropdown account links - Profile / Add Cafe / Signout links are available when a non-admin user is signed in | Pass | Profile / Add Cafe / Signout options are available to signed in non-admin users |
| | Click on Acccount link in navbar **(admin user signed in)** | Opens dropdown account links - Profile / Add Cafe / Manage Locations / Signout links are available when an admin user is signed in | Pass | Extra link available to admin users only - Manage Locations |
| | Click on Profile link in sidebar | Redirection to signed in user's Profile page | Pass | Correct session user's profile is displayed |
| | Click on Profile link in dropdown of navbar | Redirection to signed in user's Profile page | Pass | Correct session user's profile is displayed |
| | Click on Register link in dropdown of navbar | Redirection to Register page | Pass | |
| | Click on Register link in sidebar | Redirection to Register page | Pass | |
| | Click on Signin link in dropdown of navbar | Redirection to Signin page | Pass | |
| | Click on Signin link in sidebar | Redirection to Signin page | Pass | |
| | Click on Manage Locations link in dropdown of navbar | Redirection to Manage Locations page | Pass | |
| | Click on Manage Locations link in dropdown of navbar | Redirection to Manage Locations page | Pass | |
| Add Cafe button | Click on 'ADD CAFE' button (user not signed in) | Redirection to Signin page | Pass | |
|  | Click on 'ADD CAFE' button (any user signed in) | Redirection to Add Cafe page | Pass | |
| Search bar | Click on the search bar and type in a search term | Placeholder 'Search' text moves above the input field, and the search term becomes visible | Pass | |
| Search button | Once a search term is typed, click on the SEARCH button (either the recognisable magnifying glass on small devices, or the button labelled 'SEARCH' with search icon on larger devices) | The page refreshes and a list of cafe search results is displayed below the search bar (if the search returns results) or a message is displayed: "No result found" | Pass | Cafe results will only be 'found' if the search term relates to either the Cafe name / Country name / City name of saved Cafe posts. Users cannot filter results by published 'usernames' for example. |
| Reset button | Click on the RESET button (either a backwards arrow icon with or without the RESET text shown). | This will refresh the homepage, so any words typed in the search bar or searches performed will be erased. | Pass | |
| Open a published Cafe Card | Click on the Country image / Cafe name / chevron icon to expand the cafe card and reveal more information | All cafe details (matching the Add Cafe form inputs) will be visisble as the card expands | Pass | The 'published by' username and 'published on' date is also visible on the expanded cafe card|
| Close a published Cafe Card | Click on the Country image / Cafe name / chevron icon to close the expanded view | The cafe card returns to the original format of Country image / Cafe name / City name as visible to the user | Pass | Applicable to **All Pages** |
| Footer Social Links | Click the LinkedIn / Github icons | Profile pages for Tarah Waters' LinkedIn / Github will open in a new tab | Pass | Applicable to **All Pages** |
| **Register Page** | | | | |
| | Click on the Register link | Redirection to Register page | Pass | |
| Username input | Enter username on register form | Field will accept a combination of numbers and letters (5-15 characters long) in accordance with the following RegEx pattern: ^[a-zA-Z0-9]{5,15}$. | Pass | An invalid username will prompt the user with helper text in red to show there is an error. A valid username will be highlighted underneath in green and the helper text will change to "Username criteria met". A flash message will show is a username already exists in the database only after the form has been submitted. |
| Password input | Enter a valid password | Field will only password patterns as with the username format: ^[a-zA-Z0-9]{5,15}$. As with username validation, an invalid password will display red helper text to match password requirements | Pass | Registration successful - a flash massage is shown for a successful new profile / A flash error message is shown to confirm an invalid username or password |
| **Sign In** | | | | |
| | Click on the Signin link | Redirection to Signin page | Pass | |
| | Enter username on signin page | Field will accept usernames of the required format/length (as described for **Register Page**) | Pass | "Username criteria met" helper text will display in green if username meets validation criteria, otherwise the red helper text will guide the user (like on the Register page) |
| | Enter valid password on signin page | Field will only accept password of with a certain format/length | Pass | Redirection to user's Profile page with a Welcome, [username] message if successfully signed in, otherwise flash error message of "Sorry! Incorrect Username and/or Password" |
| **Sign Out** | | | | |
| | Click Signout button | Flash message will display confirmation of a successful signout, while redirecting to the homepage | Pass | |
| **Profile** | | | | |
| | Click on Profile button | User will be redirected to the Profile page | Pass | Cafe Cards published by the user will be displayed here, or if the user is 'admin', then all cafes will be displayed with EDIT / DELETE functionality|
| **Add Cafe button** | | | | |
| | Click on the ADD CAFE button | If user is signed in, they will be redirected to the 'Add Cafe' page, otherwise they will be redirected to the Signin page with a flash message: "Please signin to your account first!" | Pass | |
| **Edit Cafe button** | | | | |
| | Click on the EDIT CAFE button | The user is redirected to the Edit Cafe form with prefilled data relating to the Cafe post the button was associated with | Pass | |
| **Delete Cafe button** | | | | |
| | Click on the DELETE CAFE button | A pop up modal will display on the screen to confirm that the user wants to delete the cafe post - with YES or NO buttons to respond | Pass | A click on the YES button deletes the post from the page and display a success message. The NO button cancels the action and the user returns to the page |
| **Add / edit / delete country buttons** | | | | |
| | Click on any of the ADD COUNTRY / EDIT COUNTRY / DELETE button | Similar to the cafe buttons but this time relating to the Country cards (displaying the country name / image) | Pass | A click on the ADD COUNTRY button, redirects to the 'Add Country' page. A click on the EDIT button redirects to the prefilled country data page. A click on the YES button deletes the post from the page and display a success message. The NO button cancels the action and the user returns to the page |
| **Add Cafe form**| Once the ADD CAFE button is clicked, a page opens with the Add Cafe form. Users must input all fields and select options to submit the form with the ADD CAFE button at the bottom of the page. | Validated inputs will result in redirection to the homepage and a flash message that of "Cafe Successfully Added!". Any invalid responses will prompt the user to try again | Pass | User can then see their added cafe on the Homepage or Profile page |
| **Edit Cafe / Country form** | Click the EDIT cafe / country button | User is redirected to a prefilled form displaying either the cafe or country (admin users only) details | Pass | User can change the details and either CANCEL to return to the previous page, or save changes by clicking EDIT CAFE or EDIT COUNTRY. A success flash message will confirm any updates made. |
| **Manage Locations page** | | | | |
| | Click on the Manage Locations link | Admin user only will be redirected to the Manage Locations page | Pass | Admin user can view country cards saved to the database and either add / edit / delete countries from here |
| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile or signin page |

## User Story Testing

User stories and fatures were tested manually as shown below:

| User Story | Result |
| --- | --- |
| As a new site user and returning user, I would like to to know what the website is about and what service it is providing | A clear desciption of the website is found on the homepage |
| As a returning user, I would like to signin to my account to access my Profile and published cafes | Returning users can access the signin page via the navbar or by clicking on the ADD CAFE button |
| As a new site user, to be able to register for a secure account by creating a login username and password | New users can click on the Register link from the navbar, or the link under the Signin page. Users are redirected to the Signin page if they ever click an ADD CAFE button without being signed in |
| As a signed in user, I would like to be able to securely log out or delete the account as needed | The user cannot yet delete their account, but they can signout via the 'Signout' link which also gives them confirmation via a Flash message when it is successful |
| As a new site user and returning user, I would like to to be able to explore posts that have been shared by other users | All published cafes can be viewed from the homepage |
| As a new site user and returning user, I would like to to be able to filter more relevant posts via a search bar | All site users can filter results via the search bar on the homepage. Cafes will be displayed if there are cafe names / country names / city names that match the search terms |
| As a returning user, I would like to be able to add a post via my personal account by filling out a form and submitting it to the website database | Signed in users can add a cafe by submitted a valid Add Cafe form. A success message will be displayed, and then the cafe can be viewed from the Profile or homepage |
| As a returning user, I would like to be able to view the newly shared travel post and edit / delete if required | Edit and delete functionality it available to published cafe users from the Profile or homepage, while an admin user can edit / delete all cafes |
| As returning user, I would like to be given a warning when deleting a post, and the option to either cancel or continute with the delete action | A delete modal message will pop up to confirm the user wishes to delete a post before the action takes place. Then there is confirmation via a flash message. Or the user can cancel and return to the previous page |
| As a returning user, I would like to have confirmation that the add / edit / delete of a post action has been successful | A flash message will display a successful add / edit / delete of cafe (or country for admin users), and the resulting action can then be seen from the Profile or homepage right away |

The final user stories relate more to user experience and all links working correctly, which have been tested in Manual Testing.

## Bugs

- Delete pop-up modal was partially obstructed by cafe card content
    - to fix this, I adjusted the CSS for: .card .card-image {
z-index: 0;} - which made sure the card image is not obstructing the plane of the modal.

- Python code non-compliant e.g. lines too long (93 > 79 characters) or indentation errors etc
  - To fix these, I refactored the code to and placed breaks to make sure that it was PEP8 compliant.

- Issues with displaying all cafes to the Profile page of Admin, while only published cafes are displayed to the non-admin user's Profile
    - This involved first adding a decorator for an admin signin to be required on certain pages. Then when the Profile page is rendered, the app checks for an is_admin user in session before looping through all cafes / published user cafes. The admin user's details in the database also has the 'is_admin' attribute, which potentially could help the site have more than one admin (if their usernames are also defined in the app.py, as currently it relies on both a username and is_admin check)


## Unfixed Bugs

Some of the unfixed bugs are as noted below:

- For iOS devices, the Materialize form select settings seems to clash with the default iOS, so that for the Add Cafe form, the select inputs show both option styles. I tried a customised JS file to override this, and multiple restyling attempts, but it seems that this is an ongoing compatibility issue with Materialize and iOS. 

- The form can still be accessed and submitted successfully, but the UX is affected because of these glitches.

![Screenshot of form select glitches for iOS devices](/documentation/testing/browsers/browser-safari-mobile-error.PNG)

- Also on iOS devices, the navbar dropdown links for 'Account' can be a bit sticky - so sometimes multiple clicks are needed for the correct link to work or it needs to be reopened. This issue only seems to occur on iOS devices though which was difficult to troubleshoot and could again be a browser compatibility issue with Materialize settings.