# 📙 About
This project was essentialy just training for me to grasp more of the Django framework
<br>
This is a small and simple application made for De Boer Group, to order food on certain days, which i think turned out pretty good


# ⚙️ Setup
(skip ahead to DEPLOYMENT if you want to deploy this project to heroku straight away)
* Fork this repo (this is so you can deploy to heroku later on if you want to do so)
* Upon cloning the project, run `py -m venv .venv`
* Go into the venv by typing `.\.venv\Scripts\activate`
(if you're using VSCode you can use it as an interpreter by pressing F1 and selecting the venv)
* When you're in the venv, run `py -m pip install -r requirements.txt`
* Go to `DATABASES` in `settings.py` and set it to 
```
'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'nameYouWant.sqlite3',
    }
```
* Set `SECRET_KEY` in `settings.py` to something random (and secure), you can do so by typing <br>
```
py -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
in the terminal.
* After this run: `py manage.py makemigrations
* Followed by `py manage.py migrate`
* Go into `views.py` and put `HEROKU_RELEASE` on False

## 🤔 Optional
* Create a superuser to use in the admin by running: `py manage.py createsuperuser`. and going to `localhost/{port}/admin`

## ✔️ Finished
After all this is done, run `py manage.py runserver`

# 🚀 Deployment
To deploy this application to Heroku, first, return everything to the way it was (like it is here, on this repo)
* Fork this project
* Make a `.gitignore` and fill it with:
```
.venv/
.env
__pycache__/
nameYouChose.sqlite3
```
* Make an `.env` file, and fill it with:
```
DEBUG=False
SECRET_KEY=secret_key_you_generated_in_the_setup
DATABASE_URL=sqlite:///db.sqlite3
```
* Download the Heroku CLI, if you've not already done so
* Go into the terminal and type `heroku login` and follow the steps
* Create a heroku app by typing `heroku create nameyouwant`
* Put your secret key in heroku by typing `heroku config:set SECRET_KEY="KeyYouGeneratedDuringSetup"`
* Go into the terminal and type `deploy.bat "commit message"`
* Followed by `heroku ps:scale web=1`
* To add the database to your heroku app, type `heroku run python manage.py migrate`
* (optional) Create a superuser by typing `heroku run python manage.py createsuperuser` and follow the steps
* To view your app in the browser, type `heroku open` in the terminal

## 🐛 Debugging
The deployment may fail after deployment (server error 500) because of staticfiles, to fix this, do the following in order:
* `heroku config:set DISABLE_COLLECTSTATIC=1`
* `git push heroku main`
* `heroku run python manage.py migrate`
* `heroku run 'bower install --config.interactive=false;grunt prep;python manage.py collectstatic --noinput'`
* `heroku config:unset DISABLE_COLLECTSTATIC`
* (optional) `heroku run python manage.py collectstatic`
<br>
Check if the site still gives an error, if so, https://stackoverflow.com/questions/36665889/collectstatic-error-while-deploying-django-app-to-heroku may be of help
