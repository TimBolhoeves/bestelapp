# About
This project was essentialy just training for me to grasp more of the Django framework.
<br>
This is a small and simple application made for De Boer Group, to order food on certain days, which i think turned out pretty good.


## Setup
* Upon cloning the project, run `py -m venv .venv`. 
* Go into the venv by typing `.\.venv\Scripts\activate`. 
(if you're using VSCode you can use it as an interpreter by pressing F1 and selecting the venv). 
* When you're in the venv, run `py -m pip install -r requirements.txt`. 
* Go to `DATABASES` in `settings.py` and set it to 
```
'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'nameYouWant.sqlite3',
    }
```
* Set `SECRET_KEY` in `settings.py` to something random (and secure), you can do so by typing <br>
```
py -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'` 
```
in the terminal.
* After this run: `py manage.py makemigrations
* Followed by `py manage.py migrate`. 
* Go into `views.py` and put `HEROKU_RELEASE` on False.

## Optional
* Create a superuser to use in the admin by running: `py manage.py createsuperuser`. and going to `localhost/{port}/admin`.

## Finished
After all this is done, run `py manage.py runserver`.
