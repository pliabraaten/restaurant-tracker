
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash


# Prevents caching to allow for up to date data while in development
# MIGHT REMOVE AFTER DEVELOPMENT UNLESS NEEDED FOR REAL-TIME DATA OR USER SPECIFIC PAGES
@app.after_request # Run after each request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response



# REGISTER NEW USER
@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Register a new user. 
    - Ensures username is unique.
    - Requires password confirmation.
    - Hashes the password before saving.

    - On GET: 
    - On POST: 
    """

    return "register"


# LOG IN
@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Log in an existing user. 
    - Ensure username exists and password is correct.
    """

    return "log in"


# RESTAURANT RECORD
@app.route("/restaurant", methods=["GET", "POST"])
@login_required
def restaurant():
    """Display restaurant records"""

    return "restaurant"


# ADD NEW RESTAURANT
@app.route("/add_rest", methods=["GET", "POST"])
@login_required
def add_rest():
    """
    Create new restaurant record.
    - Name
    - Address
    - Phone number
    - Hours
    - Cuisine type
    - Ratings
    - Standard tags
    - Customizable tags
    """

    return redirect("/")


# MEAL RECORD
@app.route("/meal", methods=["GET", "POST"])
@login_required
def meal():
    """Display meal record"""

    return "meal"


# ADD NEW MEAL
@app.route("/add_meal", methods=["GET", "POST"])
@login_required
def add_meal():
    """
    Create a new meal record to an existing restaurant. 
    - Menu item name
    - Photo attachment
    - Price
    - Rating (would order again)
    - Friends present
    - Notes
    """

    return redirect("/restaurant") # Go back to restaurant page


# SEARCH FOR A RESTAURANT
@app.route("/search", methods=["GET", "POST"])
@login_required
def search():
    """
    Dynamic search for restaurants.
    Based on: 
    - Name
    - Cuisine
    - Hours
    - Ratings
    - Tags
    Sort by last visited date
    """

    return "search"


# USER PROFILE
@app.route("/user", methods=["GET", "POST"])
@login_required
def user():
    """
    Display user information.
    Allow user to change password.
    """

    return "user"

# HOME PAGE
@app.route("/")
@login_required
def index():
    """Show home page"""

    return "home page"