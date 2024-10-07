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
