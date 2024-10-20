# For premade queries for testing

from app import app, db
from app import models
from app.models import People, User, Restaurant, Meal


# Query users table
def query_users():
        users = User.query.all()
        for user in users:
            print(user.__dict__)


# Group all test queries
def main():
    with app.app_context():  # Application context
        query_users()
        ## ADD ALL NEW TEST FUNCTIONS HERE
        ## COMMENT OUT FUCTIONS IF NOT NEEDED


# Ensure the test functions only run when executed, not imported
if __name__ == "__main__":
    main()