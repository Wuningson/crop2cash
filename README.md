# crop2cash
# Introduction
Django app using Google OAuth 2.0 services for login

# Requirements
* Python3
* virtualenv
* Django
* Social-auth app Django

# Running the app
* Create a directory for the project and change into the directory
* Install the requirements
* Clone or download the repository into your directory
* Create a virtual environment by running venv -m "envname" on linux or check for the appropriate command on your operating system. (envname being anyone chose by the user) https://github.com/pypa/virtualenv
* Launch the virtual environment by running source envname/bin/activate
* Fill in the keys for SOCIAL_AUTH_GOOGLE_OAUTH2_KEY and SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET which can be gotten from https://console.developers.google.com.
* Run migrations using python manage.py migrate
* Collect static files using python manage.py collectstatic
* Run the server using python manage.py runserver
* Open browser and go to http://localhost:8000
