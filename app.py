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

        

