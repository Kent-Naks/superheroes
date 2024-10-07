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
        
        # Seeding Heroes
        print("Seeding heroes...")
        # Create a list of Hero instances
        heroes = [
            Hero(name="Kamala Khan", super_name="Ms. Marvel"),
            Hero(name="Doreen Green", super_name="Squirrel Girl"),
            Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
            Hero(name="Janet Van Dyne", super_name="The Wasp"),
            Hero(name="Wanda Maximoff", super_name="Scarlet Witch"),
            Hero(name="Carol Danvers", super_name="Captain Marvel"),
            Hero(name="Jean Grey", super_name="Dark Phoenix"),
            Hero(name="Ororo Munroe", super_name="Storm"),
            Hero(name="Kitty Pryde", super_name="Shadowcat"),
            Hero(name="Elektra Natchios", super_name="Elektra"),
        ]
        # Add all heroes to the session and commit them to the database
        db.session.add_all(heroes)
        db.session.commit()  # Commit the heroes to the database

