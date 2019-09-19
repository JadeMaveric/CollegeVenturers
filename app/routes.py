from flask import render_template
from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

user = {
    'username': 'Shawn'
}

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/leaderboard')
def leaderboard():
    projects = [
        {
            'rank': 1,
            'name': "Startup Communication",
            'link': "/project/123123", #123123 is the project id
            'domain': "Communication",
            'upvotes': 128
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
