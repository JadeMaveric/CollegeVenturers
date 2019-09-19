from flask import render_template
from app import app

user = {
    'username': 'Shawn'
}

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', user=user)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html', title='Welcome')

@app.route('/leaderboard')
def leaderboard():
    projects = [
        {
            'rank': 1,
            'name': "Startup Communication",
            'link': "/project/123123", #123123 is the project id
            'domain': "Communication",
            'tag': ['Logistics', 'Food', 'Humanities'],
            'upvotes': 12800
        }, 
        {
            'rank': 2,
            'name': "Ambulance Problem",
            'link': "/project/230123",
            'domain': "Healthcare",
            'tag': ['Logistics', 'Food', 'Humanities'],
            'upvotes': 64
        }, 
        {
            'rank': 5,
            'name': "Virtual Exhibition - Lorem ipsum dolor, sit amet consectetur adipisicing elit. Deserunt laboriosam exercitationem consequatur sapiente quaerat temporibus cumque, illo assumenda ipsam nobis!",
            'link': "/project/131103",
            'domain': "Entertainment",
            'tag': ['Logistics', 'Food', 'Humanities'],
            'upvotes': 64404
        }, 
        {
            'rank': 6,
            'name': "LOL Exhibition - Lorem ipsum dolor, sit amet consectetur adipisicing elit. Deserunt laboriosam exercitationem consequatur sapiente quaerat temporibus cumque, illo assumenda ipsam nobis!",
            'link': "/project/131303",
            'domain': "Entertainment OKAY",
            'tag': ['Logistics', 'Food', 'Humanities'],
            'upvotes': 6466
        }
    ]
    
    return render_template('leaderboard.html', title='Leaderboard', projects=projects)
