from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

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
    ])
    short_term_goal = TextAreaField('4 Week Plan', validators=[DataRequired()])
    category_primary   = StringField('Main Category', validators=[DataRequired()])
    category_secondary = StringField('Secondary Category', validators=[DataRequired()])
    category_tertiary  = StringField('Tertiary Catgeory', validators=[DataRequired()])
    submit = SubmitField('Save')
