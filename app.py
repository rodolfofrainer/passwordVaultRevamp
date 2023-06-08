from flask import Flask, render_template
from flask_login import LoginManager
from models import User

app = Flask(__name__)
login_manager = LoginManager(app)


@app.route('/')
def index():
    return render_template('login.html', title="Login Page")


@app.route('/login')
def index():
    return render_template('login.html', title="Login Page")
