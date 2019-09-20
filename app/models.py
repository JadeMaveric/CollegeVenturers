from app import db
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from hashlib import md5

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

project_contributors = db.Table('project_contributors', db.Model.metadata,
    db.Column('contributors', db.Integer, db.ForeignKey('user.id')),
    db.Column('project', db.Integer, db.ForeignKey('project.id'))
)

project_upvoters = db.Table('project_upvoters', db.Model.metadata,
    db.Column('project', db.Integer, db.ForeignKey('project.id')),
    db.Column('upvoters', db.Integer, db.ForeignKey('user.id'))
)

project_comment = db.Table('project_comments', db.Model.metadata,
    db.Column('project', db.Integer, db.ForeignKey('project.id')),
    db.Column('comment', db.Integer, db.ForeignKey('comment.id'))
)

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    # Login details
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(128), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    # Profile details
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    college = db.Column(db.String(64))
    website = db.Column(db.String(128))
    about_me = db.Column(db.Text)
    social_github  = db.Column(db.String(128))
    social_linked  = db.Column(db.String(128))
    social_twitter = db.Column(db.String(128))
    # Posts
    comments = db.relationship('Comment', backref='author', lazy='dynamic')
    upvotes  = db.relationship('Project', secondary=project_upvoters, backref='upvoters')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}'

    def __repr__(self):
        return f'<User {self.username}>'

class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    summary = db.Column(db.String(256))
    website = db.Column(db.String(128))
    description = db.Column(db.Text)
    future_scope = db.Column(db.String(32))
    short_term_goal = db.Column(db.Text)
    category_primary = db.Column(db.String(32))
    category_secondary = db.Column(db.String(32))
    category_tertiary = db.Column(db.String(32))
    comments = db.relationship('Comment', secondary=project_comment, backref='project')
    contributors = db.relationship('User', secondary=project_contributors, backref='projects')

    #rank = %COUNT(upvotes) WHERE PROJECT = self.id
    def rank(self):
        raise NotImplementedError

    def upvote_number(self):
        raise NotImplementedError

    def upvote_user_list(self):
        raise NotImplementedError

    def __repr__(self):
        return f'<Project {self.name}>'

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Comment {self.author} - {self.timestamp}>'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
    