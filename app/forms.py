from app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    firstname = StringField('Firstname', validators=[DataRequired()])
    lastname = StringField('Lastname', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    # dob = DateField('Date of birth', format='%m/%d/%Y')
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    college = StringField('College')
    website = StringField('Website')
    github = StringField('GitHub')
    linkedin = StringField('LinkedIn')
    twitter = StringField('Twitter')
    aboutme = StringField('Aboutme')
    
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
        
class ProjectForm(FlaskForm):
    name = StringField('Project Name', validators=[DataRequired()])
    summary = StringField('Short Summary', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    future_scope = SelectField('Future Scope', choices = [
      ('company', 'A company'), 
      ('ngo', 'A non-profit'),
      ('research', 'Important research'), 
      ('art', 'Iconic art work'),
      ('other', 'Something else')
    ], validators=[DataRequired()])
    short_term_goal = TextAreaField('4 Week Plan', validators=[DataRequired()])
    category_primary   = StringField('Main Category', validators=[DataRequired()])
    category_secondary = StringField('Secondary Category')
    category_tertiary  = StringField('Tertiary Catgeory')
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    text = TextAreaField('Comment Text', validators=[DataRequired()])
    submit = SubmitField('Post')
