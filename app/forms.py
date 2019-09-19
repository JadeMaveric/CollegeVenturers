from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo

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
    dob = DateField('Date of birth', format='%Y-%m-%d')
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
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
    projectDescriptionOneLine = TextAreaField('Description', validators=[DataRequired()])
    projectDescription = TextAreaField('Description', validators=[DataRequired()])
    
    
    projectWishes = SelectField('ProjectWishes', choices = [('company', 'A company'), 
      ('NGO', 'A non-profit'), ('research', 'Important research'), 
      ('art', 'Iconic art work'), """JULIUS Add other option"""])
    
    projectPlans = StringField('Description', validators=[DataRequired()])
    mainCategory = StringField('Category', validators=[DataRequired()])
    otherCategory1 = StringField('Category', validators=[DataRequired()])
    otherCategory2 = StringField('Catgeory', validators=[DataRequired()])

    submit = SubmitField('Save')
