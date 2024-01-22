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