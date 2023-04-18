PhilathropyPhinder
The project is designed to be cloned for the purpose of setting up a test environment on PyCharm IDE. It consists of a web application built on the Flask framework and includes functionality for user registration, login, searching non-profit organizations by geographical location, and sending email notifications.

Folder Structure
The project folder includes the following subfolders:

website
This folder contains all the web-framework code. The templates folder contains HTML and CSS files required for displaying web pages. The layout.html file defines the standard layout of the website, with each other HTML page derived from this one. The Flask framework is used to handle which template the user is seeing and how they interact with it. The errors, ignore, main, static and users subfolders are used for this purpose.

search
This folder contains all the backend search code and data required to perform a search on the non-profit dataset. The data folder contains geographical locations of categorized non-profit organizations in all of the 50 states, plus DC and territories. The search.py file is responsible for performing the search, selecting the data and categories that the user would like to see results from.

.idea
This folder contains all the PyCharm configuration code for testing the project.

Dependencies
The following libraries are used in the project:

Flask - for creating the web application framework
Flask_login - for handling login functionality of the website, such as registering, preventative access to certain pages and account management
CSV - for handling data pertaining to select forms, such as charity organization types
Flask_wtf - for creating a form object usable for the Flask library
Wtforms - for importing the types of forms that may be used, such as a StringField form, or a SelectMultipleField form, which just changes the type of input the form accepts.
Flask_sqlalchemy - for connecting the Flask framework to the database
Flask_bcrypt - for encrypting user data
Flask_mail - for setting up SMTP requests for sending mail through a Gmail account
Itsdangerous - for time-out requests and reset tokens for session expiration
Pandas - for loading data from CSV files to dataframes where functions can be applied
Math - for applying mathematical functions for haversine, such as radians and trigonometry
AST - for evaluating the strings containing latitude, longitude pairs as a tuple datatype.
PyCharm Configuration Steps
Clone repository to PyCharm Project
Once the project is opened, click “Add Configuration” in the top right corner
Modify script path to be path-to-your-project/run.py
Modify your Environment Variables as follows, note you will need to set up your Gmail account for application access:
PYTHONUNBUFFERED=1;SECRET_KEY=TEST;SQLALCHEMY_DATABASE_URI=sqlite:///site.db;EMAIL_USER=youremail@gmail.com;EMAIL_PASS=yourpass
Once this is configured, the site will be run on localhost ip and port 5000.
Note that this project should only be cloned to host a test environment of the project on PyCharm IDE.
