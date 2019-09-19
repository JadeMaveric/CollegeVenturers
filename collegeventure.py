from app import app, db
from app.models import Comment, User, Project

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Comment': Comment, 'Project': Project}