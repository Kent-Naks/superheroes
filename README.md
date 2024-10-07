# superheroes

-Create a new private repository on GitHub
-Git clone 
-Install dependencies
    -pipenv install
    -pipenv shell
-Set up the environment variables in a .env file. Through the migr deri through flask db init.
-export FLASK_APP=server.app:create_app
- Enter the Flask shell - flask shell



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



Had to go a complete restructure of my tree and all its code bcoz of files not being recognised within the server folder.


New structure is 
-Venv
-instance
  -superheores.db
-migration
  -versions
-app.py
-models.py
-Pipfile
-Pipfile.lock
-README.md
-requirements.txt
-seed.py


Steps.
1. pipenv install - For enev setups.
2. exit - To exit the virt env.
3. pipenv install
4. pipenv shell
5. flask db init
 ----syntax error noted.