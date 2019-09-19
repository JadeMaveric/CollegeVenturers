from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Guten Tag! Welcome to Schrute Soft Hack."
