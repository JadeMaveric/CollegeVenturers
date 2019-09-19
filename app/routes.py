from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user#, login_required
from app import app, db
from app.forms import LoginForm, RegistrationForm, CommentForm
from app.models import User
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
def index():
    return render_template('welcome.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect( url_for('index') )
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect( url_for('login') )
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect( next_page )
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect( url_for('index') )
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username = form.username.data,
            email = form.email.data,
            first_name = form.firstname.data,
            last_name = form.lastname.data,
            college = form.college.data,
            website = form.website.data,
            social_github = form.github.data,
            social_linked = form.linkedin.data,
            social_twitter = form.twitter.data,
            about_me = form.aboutme.data
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect( url_for('index') )

@app.route('/user/<username>')
#@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    projects = [
        {'id': 3,  'name': 'Whatsappify', 'upvotes': 50 },
        {'id': 17, 'name': 'Whatsappr'  , 'upvotes': 127},
        {'id': 23, 'name': 'Instagramr' , 'upvotes': 36 }
    ]
    return render_template('user.html', user=user, projects=projects)
    
@app.route('/faq')
def welcome():
    return render_template('faq.html', title='FAQs')

from datetime import datetime

@app.route('/project/<project_id>')
def project(project_id):
    comment_form = CommentForm()
    project = {
        'name': "water pollution",
        'summary': "reducing water pollution with special chemical",
        'description': "lorem ipsum bruh it's lit yo",
        'website': "http://google.com"
    }
    comments = [
        {
            'id': 1,
            'text': "Hello World!",
            'timestamp': datetime.utcnow(),
            'author': User.query.get(1)
        },
        {
            'id': 2,
            'text': "Hello World.",
            'timestamp': datetime.utcnow(),
            'author': User.query.get(1)
        },
        {
            'id': 3,
            'text': "Hello World?",
            'timestamp': datetime.utcnow(),
            'author': User.query.get(1)
        }
    ]
    return render_template('project.html', title=project['name'], project=project, comment_form=comment_form )

@app.route('/terms')
def terms():
    return render_template('terms.html', title='Terms of Service')

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
