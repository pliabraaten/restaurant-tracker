
# Standard library import
from datetime import datetime  

# Third-party imports
from flask import render_template, request, redirect, flash, url_for
from flask_login import login_required, login_user, logout_user
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
    Log out the user. 
    """
    logout_user()
    return redirect(url_for('login'))


# RESTAURANT RECORD
@app.route("/restaurant", methods=["GET", "POST"])
@login_required
def restaurant():
    """
    Display restaurant records.
    - Option to delete.
    """

    if request.method == "POST":
        # IF CLICK THE DELETE BUTTON, THEN DELETE RESTAURANT RECORD
        if request.form.get("action") == "delete_meal":
            # TODO: VERIFY THAT USER WANTS TO DELETE
            restaurant_record = Restaurant.query.filter_by(id = #TODO: ID FROM THE RESTAURANT RECORD SELETED)
            db.session.delete(restaurant_record)
            db.session.commit()

            # Redirect user back to home page
            return redirect(url_for("index"))

        # If user clicks Add Meal, then send them to mealAdd.html
        if request.form.get("action") == "add_meal":

            return render_template("mealAdd.html", rest_id = # TODO: ID OF SELECTED RESTAURANT)

    else:
        
        # TODO: GET ID FROM THE RESTAURANT RECORD OF THE REST SELECT
        # LOOKUP ALL THE DATA FIELD VALUES ASSOCIATED WITH THAT RECORD

        # TODO: QUERY ALL MEALS FOR THIS RESTAURANT IN A DICT??

        # PASS RESTAURANT AND MEAL DATA FIELD VALUES INTO THE HTML WITH THE RENDER_TEMPLATE

        # Pass in values into template (use jinja template)
        return render_template("restaurant.html", name=)
        


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

    # TODO 1ST: READ THROUGH CODE ON THIS ROUTE AND CHECK
    # TODO 2ND: GET RESTAURANTADD.HTML TO RENDER
    if request.method == "POST":
        # Capture name of new restaurant
        restaurant = request.form.get("restaurant_name")
        address = request.form.get("address")
        phone = request.form.get("phone")
        cuisine = request.form.get("cuisine")
        # rating = TODO: ADD RATING VALUE

        # Verify restaurant name was entered
        if not restaurant:
            flash("Please enter name of restaurant", "error")
            return render_template("restaurantAdd.html")
        # ADDRESS AND PHONE NUMBER OPTIONAL
        # Ensure phone number is string between 11 and 14 chars
        if len(phone) < 11 or len(phone) > 14:
            flash("Please enter a valid phone number.", "error")
            return render_template("restaurantAdd.html")
        # Ensure cuisine is selected
        if not cuisine:
            flash("Please select cuisne type for restaurant.", "error")
            return render_template("restaurantAdd.html")
        
        # TODO: ENSURE A RATING RADIO BUTTON IS SELECT

        # Check if restaurant name is already in db
        restaurant_exists = Restaurant.query.filter_by(name=restaurant).first()
        if not restaurant_exists:
            flash("Restaurant already exists.", "error")
            return render_template("restaurantAdd.html")
        # TODO: ADD BUTTON THAT REDIRECTS TO THE RESTAURANT RECORD

        # ADD RESTAURANT TO DB
        new_restaurant = Restaurant(name=restaurant, address=address, phone_number=phone, cuisine=cuisine)
        # TODO: ADD RATING TO ^ FOR THE RATION VALUE
        # TODO: ADD DATE = GET.DATE FUNCTION FOR ^
            # OR REMOVE DATE FROM RESTAURANT AND ONLY HAVE IT FOR MEAL RECORDS

        db.session.add(new_restaurant)
        db.session.commit()
        
        # Flash message for success in registering
        flash("Success! You added a new restaurant!", "success")

        # SEND USER TO RESTAURANT RECORD HTML
        return render_template("restaurant.html") # TODO: PASS IN RESTAURANT ID TO LOAD THE CORRECT RESTAURANT RECORD

    else:
        return render_template("restaurantAdd.html")


# MEAL RECORD
@app.route("/meal", methods=["GET", "POST"])
@login_required
def meal():
    """
    Display meal record.
    - Option to delete.
    """

    if request.method == "POST":
        # IF CLICK THE DELETE BUTTON, THEN DELETE meal RECORD
        # TODO: VERIFY THAT USER WANTS TO DELETE
        meal_record = Meal.query.filter_by(id = #TODO: ID FROM THE meal RECORD SELETED)
        db.session.delete(meal_record)
        db.session.commit()

        # Go back to the restaurant record
        return render_template("restaurant.html", id = #ID OF SELECTED RESTAURANT)

    else:
        
        # TODO: GET ID FROM THE meal RECORD OF THE REST SELECT
        # LOOKUP ALL THE DATA FIELD VALUES ASSOCIATED WITH THAT RECORD
        # PASS THOSE DATA FIELD VALUES INTO THE HTML WITH THE RENDER_TEMPLATE

        # Pass in values into template (use jinja template)
        return render_template("meal.html", name=)
    


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

# TODO: HOW DO I TIE THIS MEAL RECORD TO A RESTAURANT RECORD
            # THIS ROUTE IS DIRECTED ONLY FROM THE RESTAURANT RECORD RESTAURANT.HTML
            # CAN I SAVE THE RESTAURANT ID AS A SESSION VARIABLE? 
    restaurant_id = # ^^ 

    if request.method.get("POST"):
        # Capture input from forms
        meal = request.form.get("meal_name")
        price = request.form.get("price")
        #rating TODO: ADD ABILITY TO OBTAIN RATING FROM SELECTION DROPLIST
        notes = request.form.get("notes")
        person = request.form.get("person")
    
        # Verify requirement fields were entered
        if not meal: 
            flash("Please enter a name for the meal.", "error")
            return render_template("mealAdd.html")
        
        if not price or price <= 0: # TODO: or price is not a float
            flash("Please enter a valid price for the meal", "error")
            return render_template("mealAdd.html")

        # TODO: ADD VERFIFICATION FOR RATING SELECTION

        # Check if the restaurant already has this meal record existing
        meal_exists = Meal.query.filter_by(name=meal, rest_id=restaurant_id).first()  
        if not meal_exists:
            flash("This meal already exists for this restaurant", "error")
            render_template("mealAdd.html")

        # Add the meal record to the db
        new_meal = Meal(name=meal, price=price, rating=rating, person_id=person, notes=notes, rest_id_restaurant_id)

        db.session.add(new_meal)
        db.session.commit()

        # Flash message for success in registering
        flash("Success! You added a new meal!", "success")

        # SEND USER TO RESTAURANT RECORD HTML
        return render_template("restaurant.html") # TODO: PASS IN RESTAURANT ID TO LOAD THE CORRECT RESTAURANT RECORD

    else: 
        return render_template("mealAdd.html")


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

# IDEX PAGE
@app.route("/")
@login_required
def index():
    """Show home page"""
    if request.method == "POST":
        # If the add restaurant button is clicked
        if request.form.get("action") == "add_rest":
            return redirect("/add_rest")

    else:
        return render_template("index.html")