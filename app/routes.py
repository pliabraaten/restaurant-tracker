
# Standard library import
from datetime import datetime  

# Third-party imports
from flask import render_template, request, redirect, flash, url_for
from flask_login import login_required, login_user
from werkzeug.security import check_password_hash, generate_password_hash

# Local app imports
from app import app, db # Import the flask app instance and db from __init__.py
from app.models import People, User, Restaurant, Meal


# Prevents caching to allow for up to date data while in development
# TODO: MIGHT REMOVE AFTER DEVELOPMENT UNLESS NEEDED FOR REAL-TIME DATA OR USER SPECIFIC PAGES
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
    """
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        confirmation = request.form.get('confirmation')
        
        # Check if name, username, and password fields were entered
        # url_for function looks to the url for def register() instead of any hard coded /route
        if not name: 
            flash("Please enter name.", "error")
            return redirect(url_for("register"))
        if not username:
            flash("Please enter username.", "error")
            return redirect(url_for("register"))   
        if not password or not confirmation:
            flash("Please enter password twice.", "error")
            return redirect(url_for("register")) 
        
        # Check if password confirmation matches
        if password != confirmation:
            flash("Passwords must match.", "error")
            return redirect(url_for("register")) 

        # Check if username already exists in db
        username_exists = User.query.filter_by(username=username).first()  # first() retrieves first results or None
        # If username already exists
        if username_exists:
            flash("Username already exists. Please log in or try different username", "error")
            return redirect(url_for("register"))
            # TODO: ADD EASY BUTTON TO LINK TO LOGIN PAGE

        # Hash the password
        hashed_password = generate_password_hash(password)
        # Add user to people table in db
        new_person = People(name=name)
        db.session.add(new_person)
        db.session.commit()  # Get new person id
        # Add user to user table in db linking to the new record in people table
        new_user = User(username=username, password=hashed_password, person_id=new_person.id) 
        db.session.add(new_user)
        db.session.commit()
        
        # Flash message for success in registering
        flash("Success! You can now log in!", "success")

        # Log user in using flask_login feature
        login_user(new_user)

        return redirect(url_for("index"))

    # Method == GET
    else: 
        return render_template("register.html")


# LOG IN
@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Log in an existing user. 
    - Ensure username exists and password is correct.
    """
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Ensure username was entered
        if not username:
            flash("Please enter username.", "error")
            return render_template("login.html")
        
        # Ensure password was entered
        if not password:
            flash("Please enter password.", "error")
            return render_template("login.html")
        
        # Query for user record by username
        user_record = User.query.filter_by(username=username).first()

        # Check if username exists
        if not user_record:
            flash("Username does not exist.", "error")
            # TODO: ADD OPTION OR BUTTON FOR THEM TO REGISTER EASILY
            return render_template("login.html")

        # Check if password is correct
        if not check_password_hash(user_record.password, password):
            flash("Password is incorrect.", "error")
            return render_template("login.html")

        # Login in user using flask_login feature
        login_user(user_record)
        flash("Login successful!", "success")
        
        return redirect(url_for("index"))
    
    else:
        return render_template("login.html")


# LOG OUT
@app.route("/logout", methods=["GET", "POST"])
def logout():
    """
    Log in an existing user. 
    - Ensure username exists and password is correct.
    """

    return "log out"


# RESTAURANT RECORD
@app.route("/restaurant", methods=["GET", "POST"])
@login_required
def restaurant():
    """
    Display restaurant records.
    - Option to delete.
    """

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

    return redirect("/index")


# MEAL RECORD
@app.route("/meal", methods=["GET", "POST"])
@login_required
def meal():
    """
    Display meal record.
    - Option to delete.
    """

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


# LIST OF RESTAURANTS TAGGED FAVORITES
@app.route("/favorites", methods=["GET", "POST"])
@login_required
def favorites():
    """Show list of restaurants with the favorites tag"""

    return "favorites"


# USER PROFILE
@app.route("/user", methods=["GET", "POST"])
@login_required
def user():
    """
    Display user information.
    Allow user to change password.
    """

    return "user"


# ABOUT PAGE
@app.route("/about", methods=["GET", "POST"])
def about():
    """Information about the project. Like to repo?"""

    return "about"

# HOME PAGE
@app.route("/")
@login_required
def index():
    """Show home page"""

    return render_template("index.html")