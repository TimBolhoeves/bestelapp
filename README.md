# Setup
Upon cloning the project, run `py -m venv .venv`
Go into the venv by typing `.\.venv\Scripts\activate`
(if you're using VSCode you can use it as an interpreter by pressing F1 and selecting the venv)
When you're in the venv, run `pip install -r requirements.txt`
After this run: `py manage.py makemigrations`
Followed by `py manage.py migrate`
And an optional superuser to use in the admin by running: `py manage.py createsuperuser`

After all this is done, run `py manage.py runserver`
