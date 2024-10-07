# Imports and Setup
from random import choice as rc  # Importing choice function for random selection
from app import app, db  # Importing the Flask app and database instance
from models import Hero, Power, HeroPower  # Importing the models for seeding

# Entry point for the script
if __name__ == '__main__':
    with app.app_context():  # Ensure the application context is available for database operations
        print("Clearing db...")
        # Clear existing records from the database
        Power.query.delete()  
        Hero.query.delete()  
        HeroPower.query.delete()
