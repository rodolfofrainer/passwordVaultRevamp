from flask_login import UserMixin
import bcrypt
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @staticmethod
    def get(user_id):
        # Retrieve user from the database based on user_id
        # Example implementation:
        # return User.query.get(int(user_id))
        return None

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
