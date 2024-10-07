from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import validates

# Initialize the Flask application
app = Flask(__name__)

# Configuring the database to use SQLite with a specified database file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
# Disable track modifications to reduce overhead
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Migrate for database management
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Importing model classes after initializing SQLAlchemy to avoid circular imports
from models import Hero, Power, HeroPower

# Routes for the Hero resource
@app.route('/heroes', methods=['GET'])
def get_heroes():
    # Retrieve all heroes from the database and return them as JSON
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes])

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    # Retrieve a specific hero by ID and return it as JSON
    hero = Hero.query.get(id)
    if hero:
        return jsonify(hero.to_dict())
    else:
        return jsonify({"error": "Hero not found"}), 404


        

