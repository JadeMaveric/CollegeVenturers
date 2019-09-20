## College Venturers
Gamification and Discovery to boost college projects!
College projects are an untapped resource! Do you have a startup/business idea? Are you a student working on something that could be a startup someday? Submit it on College Venturers and get discovered!

![College Venturers](https://user-images.githubusercontent.com/43012143/65302449-d8c7de80-db98-11e9-8775-f120d871bd04.jpeg)

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

We recommend using a venv to run the project.  
Run ```pip install -r requirements.txt``` to install the necessary packages.  
```flask run``` will start the server on port 5000.  
```flask db init``` will initialise the database.  
```flask db migrate``` and the ```flask db upgrade``` will get it up and running.  
Use ```flask shell``` to pop into an interactive python session. Useful for testing queries.  

Directory Structure:  
.flaskenv --environment variable required to run the project.  
collegeventure.py --main file that is run.  
config.py --configurations for various objects used throughout the project.  
requirements.txt -- list of libraries used. output of pip freeze.  
app/ --main app files  
  __init__.py --initialises objects used throughtout the project  
  forms.py --flask-WTForms (used for login, registration, comment, etc...)  
  models.py --DBMS Models  
  routes.py --server endpoints and authentication  
  templates/  
    various html templates
  static/
    static files served along with the html files
