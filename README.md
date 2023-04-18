# PhilanthropyPhinder
This project should only be cloned to host a test environment of the project on PyCharm IDE.

## Website
All web-framework code is located in the folder **website**.

### Templates
All HTML and CSS files that are required to create displayable pages are located in this folder. **layout.html** defines the standard layout of our site, with each other HTML page derived from this one. These were all developed by Javon Mais.

### Flask Framework
**errors**, **ignore**, **main**, **static**, and **users** are all the remaining folders in the framework that are used to handle which template the user is seeing and how they interact with it. This section was mainly developed by Adam Essaydi with minor updates from Andrew Wernersbach and Javon Mais.

### Main
**routes.py** is responsible for ensuring the home page is displayed from the app, using Flask library requests, blueprints.

### Errors
Contains error handlers from Flask, with the codes and the error pages that will be displayed if the website encounters an error.

### Users
Contains most of the user interactive behavior. Many libraries are used and will be described below:

Flask_login: used to handle the login functionality of the website, such as registering, preventative access to certain pages, and account management

CSV: used to handle data pertaining to select forms, such as charity organization types

Flask_wtf: used to create a form object usable for the Flask library

Wtforms: used to import the types of forms that may be used, such as a **StringField** form or a **SelectMultipleField** form, which just changes the type of input the form accepts.

Flask_sqlalchemy: used to connect the Flask framework to the database

Flask_bcrypt: used to encrypt user data

Flask_mail: used to set up SMTP requests for sending mail through a Gmail account

Itsdangerous: used for time-out requests and reset tokens for session expiration

Os: used to set and fetch environment variables and settings for the system

All backend search code and data are stored within **search**.

## Search
Contains all functionality required to perform a search on our non-profit dataset from the backend. This section was developed by Andrew Wernersbach.

### Data
data folder contains geographical locations of categorized non-profit organizations in all of the 50 states, plus DC and territories.

### Search.py
Responsible for performing the search, selecting the data and categories that the user would like to see results from. Libraries are described below:

Pandas: Used to load data from CSV files to dataframes where functions can be applied.

Math: Used to apply mathematical functions for haversine, such as radians and trigonometry.

AST: Used to evaluate the strings containing latitude, longitude pairs as a tuple datatype.

OS: Used to locate the data folder on the deployment system.

All PyCharm configuration code (for testing) are stored in .idea folder.

## PyCharm Configuration Steps
1. Clone repository to PyCharm Project
2. Once project is opened, click “Add Configuration” in the top right corner
3. Modify script path to be path-to-your-project/run.py
4. Modify your Environment Variables as follows, note you will need to set up your Gmail account for application access:

PYTHONUNBUFFERED=1;
SECRET_KEY=TEST;
SQLALCHEMY_DATABASE_URI=sqlite:///site.db;
EMAIL_USER=youremail@gmail.com;
EMAIL_PASS=yourpassword

Once this is configured, site will be run on localhost IP and port 5000.

Note: Replace `path-to-your-project` with your project path.
