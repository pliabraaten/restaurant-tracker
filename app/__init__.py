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

# TODO: INITIALIZE FLASK-LOGIN AND LOGINMANAGER TO FINISH FLASK SETUP FOR WEB PAGE TESTING


# Import routes after Flask app is created
from app import routes, models