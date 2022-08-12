# Setup
Upon cloning the project, run `py -m venv .venv`. \n
Go into the venv by typing `.\.venv\Scripts\activate`. \n
(if you're using VSCode you can use it as an interpreter by pressing F1 and selecting the venv). \n
When you're in the venv, run `pip install -r requirements.txt`. \n
After this run: `py manage.py makemigrations`. \n
Followed by `py manage.py migrate`. \n
And an optional superuser to use in the admin by running: `py manage.py createsuperuser`. \n
\n
After all this is done, run `py manage.py runserver`.
