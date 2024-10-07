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
