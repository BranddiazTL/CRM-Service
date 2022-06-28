# CRM-Service

## Project Set-Up

The project is build for easy set up in any environment, the only thing you
will need is Docker in your system.

After installing Docker you can clone the repo from:

    git clone https://github.com/BranddiazTL/CRM-Service.git

Now in the root directory of the project you can use the command:

    docker-compose up --build
    
This command will trigger the creation of the PostgreSQL database and
the Django project specified on the Docker Compose file. The --build flag
tells docker to install all of our dependencies on the requirements.txt file
so we only need to use this flag in the first run, or if we need a new dependency.

In any other instance we use:

    docker-compose up
    
Now our project is ready to use on the default :8000 port on our localhost.

After we finish using the project we need to stop the currently running 
container with "Control + c" and additionally type:
 
    docker-compose down 
    
in the root terminal. 

Docker containers take up a lot of memory so it's a good idea to stop them when we are done using them.

## How to Use the Project

Now that we now how to set up the project, we need to know how to use it. 
Our project has 2 parts, the Admin side, and the API.

Admin Side:

You can visit the side on 

http://localhost:8000/admin/

In there you will find a Login form, you can create an Admin User as follows:

    docker-compose exec app python manage.py createsuperuser


In the admin side you will find that you can 
+ Manage and create new users
+ Manage and create new customers 
+ Manage and create new customers OAuth2 Applications (that will auto generate the client
ID and the client secret)

When you add a new user you can set if that user 
has permissions to manage the Customers or not, and if you want the user to
been able to Login to the admin side be setting the user as STAFF and adding
the Customers permissions on the EDIT page.

API:

Now that you have your OAuth2 application you can use the Login method
to Authenticate on the API and create and manage the Customers information.

POST http://localhost:8000/o/token/ Json Body

On this endpoint you will send the Application client information in a JSON
Body like this:

    {   
        "grant_type": "password",
        "client_id": "U8hUqOes3nDv3CqUrLIXcQMlExWIO8jLZQEwdhNi",
        "username": "admin",
        "password": "admin"
    }

With that you will receive a JSON response with your Bearer token:

    {
        "access_token": "ewnGy6y2bkUmzGi7Pz9DoGqgCpnXzZ",
        "expires_in": 36000,
        "token_type": "Bearer",
        "scope": "read write groups",
        "refresh_token": "euwNlIwpwHziWhXfowWAbe26ccZVMF"
    }

Now you can uses all the Customer endpoints to GET and manage the customers,
you can access the API Documentation to see the available endpoints and request schemas:

http://localhost:8000/docs/

Now that you are familiar with the endpoints you can go ahead and use 
the endpoints with the token you receive from the Login endpoint.

You only need to sent the following Header:

    Key               Value
    
    Authorization     Bearer {token}
    
And that is it, you now have access to GET, POST, PUT, PATCH and DELETE 
of Customers.


## How to Make the Django Project Boiler Plate from Scratch

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