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

# Section 3: Power Routes
# Routes for the Power resource
@app.route('/powers', methods=['GET'])
def get_powers():
    # Retrieve all powers from the database and return them as JSON
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers])

# Routes for the Power resource
@app.route('/powers', methods=['GET'])
def get_powers():
    # Retrieve all powers from the database and return them as JSON
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers])

@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    # Retrieve a specific power by ID and return it as JSON
    power = Power.query.get(id)
    if power:
        return jsonify(power.to_dict())
    else:
        return jsonify({"error": "Power not found"}), 404

# Route to update a specific power's description
@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    # Retrieve the power by ID
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    # Get the request data
    data = request.get_json()
    description = data.get('description')

    # Validate that the description is at least 20 characters long
    if description and len(description) >= 20:
        power.description = description
        db.session.commit()
        return jsonify({
            "id": power.id,
            "name": power.name,
            "description": power.description
        }), 200
    else:
        return jsonify({"errors": ["Description must be at least 20 characters long."]}), 400

# Handle both GET and POST methods for hero powers
@app.route('/hero_powers', methods=['GET', 'POST'])
def hero_powers():
    if request.method == 'POST':
        # Handle the creation of a new HeroPower association
        data = request.get_json()
        strength = data.get('strength')
        hero_id = data.get('hero_id')
        power_id = data.get('power_id')

        # Validate strength input
        if strength not in ['Strong', 'Weak', 'Average']:
            return jsonify({"errors": ["Strength must be 'Strong', 'Weak', or 'Average'."]}), 400

        # Validate the existence of the specified hero and power
        hero = Hero.query.get(hero_id)
        power = Power.query.get(power_id)

        if not hero or not power:
            return jsonify({"errors": ["Hero or Power not found."]}), 404

        # Create a new HeroPower association and save to the database
        hero_power = HeroPower(strength=strength, hero_id=hero_id, power_id=power_id)
        db.session.add(hero_power)
        db.session.commit()

        # Return the details of the new HeroPower association as JSON
        return jsonify({
            "id": hero_power.id,
            "strength": hero_power.strength,
            "hero_id": hero.id,
            "power_id": power.id,
            "hero": {
                "id": hero.id,
                "name": hero.name,
                "super_name": hero.super_name
            },
            "power": {
                "id": power.id,
                "name": power.name,
                "description": power.description
            }
        }), 201

    elif request.method == 'GET':
        # Retrieve all HeroPower associations and return them as JSON
        hero_powers = HeroPower.query.all()
        return jsonify([{
            "id": hero_power.id,
            "strength": hero_power.strength,
            "hero_id": hero_power.hero_id,
            "power_id": hero_power.power_id,
            "hero": hero_power.hero.to_dict(),
            "power": hero_power.power.to_dict()
        } for hero_power in hero_powers])

# Run the application in debug mode
if __name__ == '__main__':
    app.run(debug=True)
