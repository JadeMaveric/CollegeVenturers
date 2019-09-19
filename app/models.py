from app import db
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    # Login details
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    # Profile details
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    college = db.Column(db.String(64))
    website = db.Column(db.String(120))
    about_me = db.Column(db.Text)
    social_github  = db.Column(db.String(120))
    social_linked  = db.Column(db.String(120))
    social_twitter = db.Column(db.String(120))
    # Projects

    # Upvotes
    upvotes = db.relationship('Post', backref='user', lazy='dynamic') 
    # Comments

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
    