import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user
from models import User
from dotenv import load_dotenv
from datetime import timedelta

app = Flask(__name__)
load_dotenv()
app.secret_key = os.environ.get("SECRET_KEY")
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    # Load the user based on the user_id
    return User.get(user_id)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Retrieve user from the database based on the username
        # Example implementation:
        # user = User.query.filter_by(username=username).first()
        user = User(1, 'example_user', 'example_password')

        if user and user.check_password(password):
            login_user(user)  # Log in the user
            flash('Login successful!', 'success')
            # Redirect to a protected page
            return redirect(url_for('protected'))
        else:
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))

    return render_template('login.html', title="Login Page")


@app.route('/')
def index():
    return render_template('index.html', title="Home Page")


@app.route('/protected')
@login_required
def protected():
    return render_template('protected.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()  # Log out the user
    flash('You have been logged out', 'info')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
