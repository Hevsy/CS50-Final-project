# Travel Companion

**Final Project for CS50x Course**

This is a web application built with Flask, SQLAlchemy, MySQL, HTML/CSS, and JavaScript that allows users to store and organize their travel plans and activities.

### Video Demo:  <URL HERE>

## Description

The Travel Companion app allows users to create notebooks for their travel plans, where they can store ideas, places of interest, and links organized by destination. The app includes features such as user registration and authentication, creating, editing, and deleting notebooks, adding and removing destinations from notebooks, and adding and editing notes, links, and ideas for each destination.

## Installation
To install and run *Travel Companion* in a test mode, follow these steps:

- Clone or download the repository to your local machine
- Create a virtual environment with Python 3: `python3 -m venv env`
- Install the required packages with `pip install -r requirements.txt.`
- Create `etc/.env` file with your environment and database configurations. You can use the example file `etc/.env.example` as a template
- Run `python3 app.py` to start the application
- Visit `http://localhost:5000` in your web browser to access the app

For a production environment, it's recommended to use a WSGI server like Gunicorn in combination with the steps outlined above. Additionally, for improved security and performance, a reverse proxy server like Nginx or Apache can be configured as the primary client-facing web server.

## Files

- app.py: The main application file containing the Flask app and routes
- requirements.txt: A list of Python packages required for the application to run
- etc/.env.example: An example `.env` file containing environment variables required by the application
- etc/config.py: A configuration file that loads the environment variable file and creates the database configuration based on it
- etc/db_init.py: A module that creates the database engine and tables required by the application
- etc/functions.py: A module that contains all non-primary functions of the app, eg functions that are called by the routes in `app.py` or any other functionality that is not directly related to routing
- static/favicon.ico: The app's favicon
- static/styles.css: The app's CSS styling (Based on SB Admin 2 template)
- templates/: A folder containing HTML templates for different pages of the app

## Design choices

Initially, I was planning to use Django framework, but it is notoriously challenging to master and I pivoted to Flask as a familiar ground, so I could spend more time on actual design and coding.

I am planning to eventually put this application out on the web, so I was designing backend with real world scenarios in mind. Primarily it resulted in using MySQL as the backend database for its scalability and reliability. I am well versed in AWS services, so putting such a database on AWS RDS service will be an easy task. 
I was debating between PostgreSQL and MySQL, but I already used Postgres for my other projects, so decided to try MySQL to get some experience with it. SQLAlchemy was chosen to interact with the MySQL database. I’ve separated all DB configuration and initialization routines into separate modules `etc\config.py` and `etc\db-init.py`, so the main app could be DB-agnostic.

At first, I got all DB credentials hardcoded into the `config.py`, but to follow recommended security practices, I moved them to environmental variables and later amended `config.py` to cater for DEV/TEST/PROD environments.

For UI and frontend, I decided to use Bootstrap and the [StartBootsrtap Admin 2 template](https://startbootstrap.com/theme/sb-admin-2) for the HTML styling. This allowed me to quickly create a professional-looking interface without having to spend a lot of time on CSS. Still, I ended up spending a bit of time refining the template to upgrade it from Bootsrap 4 to Boostrap 5.