# Creates the Flask app instance - ties configs, routes, and other components

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

# Initialize Flask app
app = Flask(__name__)

# Load configurations from config.py
app.config.from_object(Config)

# Initialize SQLAlchemy with the app
db = SQLAlchemy(app)

# Set up LoginManger from Flask-Login
login_manager = LoginManager(app)
# Redirects users not logged in to the /login route when attempting to access routes that require login
login_manager.login_view = 'login'  

# Flask-Login stores user ID when they log in
@login_manager.user_loader  # Calls this function to load user from db
def load_user(user_id):  # Loads user_id of currently logged-in user
        return User.query.get(int(user_id))  # DB lookup of the user with the user_id from current session


# Import routes after Flask app is created
from app import routes, models