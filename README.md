# About
This project was essentialy just training for me to grasp more of the Django framework.
<br>
This is a small and simple application made for De Boer Group, to order food on certain days. 


## Setup
* Upon cloning the project, run `py -m venv .venv`. 
* Go into the venv by typing `.\.venv\Scripts\activate`. 
(if you're using VSCode you can use it as an interpreter by pressing F1 and selecting the venv). 
* When you're in the venv, run `pip install -r requirements.txt`. 
* After this run: `py manage.py makemigrations`. 
* Followed by `py manage.py migrate`. 

## Optional
* Create a superuser to use in the admin by running: `py manage.py createsuperuser`. and going to localhost/{port}/admin
* Go into `views.py` and put `DEPLOYMENT` on false.

## Finished
After all this is done, run `py manage.py runserver`.
