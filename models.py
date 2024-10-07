from app import db

# Hero Model
class Hero(db.Model):
    __tablename__ = 'heroes'  # Name of the database table
    id = db.Column(db.Integer, primary_key=True)  # Primary key for the hero
    name = db.Column(db.String, nullable=False)  # Hero's name
    super_name = db.Column(db.String, nullable=False)  # Hero's superhero alias
    # Relationship to HeroPower with cascade delete for orphan records
    hero_powers = db.relationship('HeroPower', backref='hero', cascade='all, delete-orphan')

    def to_dict(self):
        # Convert Hero instance to a dictionary for JSON representation
        return {
            "id": self.id,
            "name": self.name,
            "super_name": self.super_name
        }

    def to_dict_with_powers(self):
        # Convert Hero instance to a dictionary, including hero powers
        return {
            "id": self.id,
            "name": self.name,
            "super_name": self.super_name,
            "hero_powers": [hp.to_dict() for hp in self.hero_powers]  # Include hero powers in the dict
        }

# Power Model
class Power(db.Model):
    __tablename__ = 'powers'  # Name of the database table
    id = db.Column(db.Integer, primary_key=True)  # Primary key for the power
    name = db.Column(db.String, nullable=False)  # Name of the power
    description = db.Column(db.String, nullable=False)  # Description of the power
    # Relationship to HeroPower with cascade delete for orphan records
    hero_powers = db.relationship('HeroPower', backref='power', cascade='all, delete-orphan')

    def __init__(self, name, description):
        # Initialize Power instance with name and description
        self.name = name
        self.description = description

    @staticmethod
    def validate_description(description):
        # Validate the length of the power's description
        if len(description) < 20:
            raise ValueError('Description must be at least 20 characters long')

    def to_dict(self):
        # Convert Power instance to a dictionary for JSON representation
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }

# HeroPower Model
class HeroPower(db.Model):
    __tablename__ = 'hero_powers'  # Name of the database table
    id = db.Column(db.Integer, primary_key=True)  # Primary key for the association
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))  # Foreign key to the Hero table
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))  # Foreign key to the Power table
    strength = db.Column(db.String, nullable=False)  # Strength level of the association

    def __init__(self, hero_id, power_id, strength):
        # Initialize HeroPower instance with hero and power IDs, and strength
        self.hero_id = hero_id
        self.power_id = power_id
        self.strength = strength

    @staticmethod
    def validate_strength(strength):
        # Validate the strength value
        if strength not in ['Strong', 'Weak', 'Average']:
            raise ValueError('Invalid strength value')

    def to_dict(self):
        # Convert HeroPower instance to a dictionary for JSON representation
        return {
            "id": self.id,
            "hero_id": self.hero_id,
            "power_id": self.power_id,
            "strength": self.strength,
            "hero": self.hero.to_dict(),  # Include hero details
            "power": self.power.to_dict()   # Include power details
        }

