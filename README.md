# crop2cash
Django app using Google OAuth 2.0 services for login
The folder structure has the OAuth which is the main project and the pages app. 
social-auth-app-django is installed through the python installation package manager
The urls and views file was created for the pages app and functions defined.
The templates folder with the index.html file and the base.html files were created. The base.html file contains the base template and the index contains the markup for the page displaying the details of a logged in user or creates a new user. This is achieved through jinja tags using if else statements.
The directory for the templates is added in the settings.py file.
The settings for the django auth app are set up in the settings.py app as well as the google's oauth configurations.
