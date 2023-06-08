from flask_login import UserMixin
import bcrypt
from dotenv import load_dotenv
from database import db
import os

# load environment variables
load_dotenv()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        # Hash, salt, and pepper the provided password
        salt = bcrypt.gensalt()
        pepper = os.environ.get("PEPPER").encode()
        hashed_password = bcrypt.hashpw(password.encode(), salt + pepper)
        self.password = hashed_password

    def check_password(self, password):
        # Compare the provided password with the stored password
        salt = bcrypt.gensalt()
        pepper = os.environ.get("PEPPER").encode()
        hashed_password = bcrypt.hashpw(password.encode(), salt + pepper)
        return bcrypt.checkpw(password.encode(), hashed_password)
