from flask_login import UserMixin


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

    def check_password(self, password):
        # Compare the provided password with the stored password
        return password == self.password
