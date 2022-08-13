# About
This project was essentialy just training for me to grasp more of the Django framework.
<br>
This is a small and simple application made for De Boer Group, to order food on certain days, which i think turned out pretty good.


## Setup
* Upon cloning the project, run `py -m venv .venv`. 
* Go into the venv by typing `.\.venv\Scripts\activate`. 
(if you're using VSCode you can use it as an interpreter by pressing F1 and selecting the venv). 
* When you're in the venv, run `py -m pip install -r requirements.txt`. 
* Set database settings back to default (if you're not using an `.env` to set database settings), for more information, visit: [Django database settings](https://docs.djangoproject.com/en/4.1/ref/settings/#databases)
* After this run: `py manage.py makemigrations`. 
* Followed by `py manage.py migrate`. 
* Go into `views.py` and put `DEPLOYMENT` on False.

## Optional
* Create a superuser to use in the admin by running: `py manage.py createsuperuser`. and going to localhost/{port}/admin

## Finished
After all this is done, run `py manage.py runserver`.
