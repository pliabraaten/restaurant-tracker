# Configuration and Initialization Files

```
project_root/
|-- run.py         # imports and runs the Flask app
|-- config.py      # contains configuration settings, applied in __init__.py
|-- app/
|   |-- __init__.py   # creates Flask app, configures it, and imports models and routes
|   |-- routes.py     # handles routes and imports models
|   |-- models.py     # defines database models, db initialized in __init__.py
```

**Overview**

The Restaurant Tracker is a web application built using Python, Flask, and SQLAlchemy. This app helps users keep track of their dining experiences by allowing them to add and manage restaurant records, associate meal records with specific restaurants, and search for restaurants based on various criteria. Users can also review past meals to decide where to eat next and what to order.


**USER STORIES AND TASKS**
-------------------------------------------------------------------------------------------------------------------
1. **Account Management**

   **User Story**: As a user, I want to create an account and log in securely to manage my data.

   **Tasks**:
   - Create routes for registering, logging in, and logging out.
   - Hash passwords for security.

2. **Adding Restaurants**

   **User Story**: As a user, I want to add restaurants with details like name, address, and cuisine to track where I’ve eaten.

   **Tasks**:
   - Create a form to add restaurant details.
   - Prevent duplicate restaurant entries.

3. **Adding Meals**

   **User Story**: As a user, I want to add meals to restaurants with tags and ratings to remember my experiences.

   **Tasks**:
   - Create a form to add meals to a restaurant.
   - Link meals to specific restaurants.

4. **Searching for Restaurants**

   **User Story**: As a user, I want to search for restaurants by name, cuisine, or tags to decide where to eat.

   **Tasks**:
   - Add a search form for restaurant filters.
   - Use filters like name, cuisine, and rating.

5. **Viewing Details**

   **User Story**: As a user, I want to view restaurant and meal details to review past dining experiences.

   **Tasks**:
   - Display restaurant information and its associated meals on one page.

6. **Editing and Deleting**

   **User Story**: As a user, I want to edit or delete restaurants and meals to keep my data up to date.

   **Tasks**:
   - Create routes and forms for editing and deleting records.



