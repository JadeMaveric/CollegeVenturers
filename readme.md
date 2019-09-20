## College Venturers

Project for Inspirathon, the Hackathon at Inspirus 2019.

Team members:

- [Julius Alphonso](https://github.com/JadeMaveric)
- [Shawn Pereira](https://github.com/recurshawn)
- [Vipul Chodankar](https://github.com/vipulchodankar)

Technology Stack:

- Front-end:
  - HTML, CSS, JavaScript
- Back-end:
  - Python - Flask

We recommend using a venv to run the project
run ```pip install -r requirements.txt``` to install the necessary packages
```flask run``` will start the server on port 5000
```flask db init``` will initialise the database
```flask db migrate``` and the ```flask db upgrade``` will get it up and running
use ```flask shell``` to pop into an interactive python session. Useful for testing queries

Directory Structure:
.flaskenv --environment variable required to run the project
collegeventure.py --main file that is run
config.py --configurations for various objects used throughout the project
requirements.txt -- list of libraries used. output of pip freeze
app/ --main app files
  __init__.py --initialises objects used throughtout the project
  forms.py --flask-WTForms (used for login, registration, comment, etc...)
  models.py --DBMS Models
  routes.py --server endpoints and authentication
  templates/
    various html templates
  static/
    static files served along with the html files
