# Entry point for Flask app - imports Flask app instance and starts the app

# Import app instance and db instance from __init__.py
from app import app

print("Starting Flask application...")
print(f"App object: {app}")

# If this run.py file is being run directly (not imported), then start Flask's development web server in debug mode
if __name__ == '__main__':
    app.run(debug=True)  # OMIT DEBUG MODE FOR PRODUCTION ENVIRONMENT

