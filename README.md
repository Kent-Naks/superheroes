# superheroes

-Create a new private repository on GitHub
-Git clone 
-Install dependencies
    -pipenv install
    -pipenv shell
-Set up the environment variables in a .env file

Created a skeleton tree structure, to guide me through the project. Subject to change:

── migrations/
   ── versions/    # Alembic migration scripts
── server/
   ── __init__.py  # Initializes Flask app and database
   ── app.py       # Contains the application entry point
   ── models.py    # Defines Hero, Power, and HeroPower models
   ── routes.py    # Handles the routes for the API
   ── seed.py      # Seeds the database with initial data
   ── serializers.py  # Serializes data for proper JSON responses
   ── validations.py  # Custom validation logic

── tests/
   ── test_routes.py  # Tests for all API endpoints

── .env             # Environment variables (e.g., DB_URI)
── README.md        # Project description and instructions
── Pipfile          # Pipenv file (optional, if you use Pipenv)
── alembic.ini      # Alembic configuration for migrations
── challenge-2-superheroes.postman_collection.json  # Postman collection
