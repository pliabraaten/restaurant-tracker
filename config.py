# Configuration settings for different environments (dev, production, testing)

# Imports os module which is used to access environment variables
import os

# Create class for the configuration settings
class Config:
    
    # TODO: SET ENVIRONMENT SECRET KEY VARIABLE OR CHANGE THE "YOU-WILL-NEVER-GUESS" STRING TO A SECURE STRING FOR PRODUCTION
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
    # Sets URI (Uniform Resource Identifier) to the sqlite db if the DATABASE_URL environment is not set
    # TODO: FOR PRODUCTION, SET DATABASE_URL ENVIRONMENT VARIABLE
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///restaurants.db'
    
    # Disables feature signaling every change in the db
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# TODO: FIGURE OUT HOW TO USE THESE AND IF THEY ARE NEEDED IN THIS PROJECT
# class DevelopmentConfig(Config):
#     DEBUG = True

# class ProductionConfig(Config):
#     DEBUG = FALSE

### IF ^ ADDED, MODIFY __INIT__.PY FILE FOR MULTIPLE ENVIRONMENT CONFIGURATIONS, SOMETHING LIKE THIS
    # if os.environ.get('FLASK_ENV') == 'production':
    #     app.config.from_object('config.ProductionConfig')
    # else:
    #     app.config.from_object('config.DevelopmentConfig')
