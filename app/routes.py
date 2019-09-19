from flask import render_template
from app import app

user = {
    'username': 'Shawn'
}

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', user=user)

@app.route('/leaderboard')
def leaderboard():
    projects = [
        {
            'rank': 1,
            'name': "Startup Communication",
            'link': "/project/123123", #123123 is the project id
            'domain': "Communication",
            'upvotes': 0
        }, 
        {
            'rank': 2,
            'name': "Ambulance Problem",
            'link': "/project/230123",
            'domain': "Healthcare",
            'upvotes': 0
        }
    ]
    
    return render_template('leaderboard.html', title='Leaderboard', projects=projects)
