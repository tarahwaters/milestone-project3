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
| Edit Country (admin) | Mobile | ![screenshot](documentation/lighthouse-addgift-mobile.png) | Slow response time due to large images |
| Edit Country (admin) | Desktop | ![screenshot](documentation/lighthouse-addgift-desktop.png) | Slow response time due to large images |