# CRM-Service

## How to Make the Project from Scratch

The first step is to install the desktop Docker app for your local machine:

- __[Docker for Mac](https://docs.docker.com/docker-for-mac/install/)__
- __[Docker for Windows](https://docs.docker.com/docker-for-windows/install/)__ 
- __[Docker for Linux](https://docs.docker.com/install/)__  


And Python if you dont have it:

- __[Python for Mac](https://www.python.org/downloads/mac-osx)__
- __[Python for Windows](https://www.python.org/downloads/windows)__ 
- __[Python for Linux](https://www.python.org/downloads/source/)__  

Now we install Django, in Python we always need a virtual environment or VENV.

    # Windows  
    $ python -m venv .venv
    $ Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    $ .venv\Scripts\Activate.ps1
    (.venv) $ python -m pip install django
    
    # MacOS
    $ python3 -m venv .venv
    $ source .venv/bin/activate
    (.venv) $ python3 -m pip install django
    
Now we create the Django Project, we migrate the first the default database
data that Django stores in a sqlite3 database and we run the project to see
if everything is working fine, by default Django runs on http://127.0.0.1:8000/

    (.venv) $ django-admin startproject django_project .
    (.venv) $ python manage.py migrate
    (.venv) $ python manage.py runserver
    
Now we use the PIP Freeze command to get the depencies that Django has by
default and created a requirements.txt to save the dependencies

    (.venv) $ pip freeze > requirements.txt
    
Them we edit the file adding the postgres and test depencies, at the end
the file needs to look something like this:

    asgiref==3.5.2
    Django==4.0.5
    sqlparse==0.4.2
    psycopg2-binary==2.9.3
    pylint==2.12.2
    pylint-django==2.5.2
    pylint-plugin-utils==0.7
    flake8 >= 3.0.0
    unittest-xml-reporting==3.2.0
    
To exit the server that is running we use CTRL + C, and to exit from the 
VENV enviorement we use the command 'deactivate'

    (.venv) $ deactivate
    
To be continue...