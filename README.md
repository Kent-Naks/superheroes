# Superhero Management Application
Overview

-Ni nini: Hii ni web application ya kusimamia superheroes na nguvu zao.
-Teknolojia: Imejengwa kwa Flask, SQLAlchemy, na SQLite kwa usimamizi wa database.
-Kazi: Inakuwezesha kufanya operesheni za CRUD kwenye mashujaa na nguvu zao, na kuziunganisha pamoja.


-Create a new private repository on GitHub
-Git clone 
-Install dependencies
    -pipenv install
    -pipenv shell
-Set up the environment variables in a .env file. Through the migr deri through flask db init.
-export FLASK_APP=server.app:create_app
- Enter the Flask shell - flask shell



Skeleton Tree Structure: Nilijenga muktadha wa miti kuongoza kwenye mradi. Huu unaweza kubadilika:

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



Restructured Tree: Nililazimika kubadilisha muundo wa mti wangu kwa sababu ya faili ambazo hazikutambuliwa ndani ya folda ya server.


Muundo Mpya:

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
5. installing required packages - pip install Flask Flask-SQLAlchemy Flask-Migrate
6. flask db init
 ----syntax error noted.
7. flask db init
   flask db migrate
   flask db upgrade
8. Running the application - python app.py
9. Seeding the DATABASE - python seed.py
10. API Endpoints:

Retrieve all heroes: GET /heroes
Access a specific hero by ID: GET /heroes/<id>
Atain all powers: GET /powers
Achieve a specific power by ID: GET /powers/<id>
Update a power's description: PATCH /powers/<id>
Retrieve all hero-power associations: GET /hero_powers
Create a new hero-power association: POST /hero_powers

The fial file description:
app.py

-Madhumuni: Kipengele kikuu cha kuingia kwa programu.
-Makala Muhimu:
  -Inaagiza Flask, SQLAlchemy, na Migrate.
  -Inajiandaa na kuanzisha Flask app na kuunda SQLite kama database.
  -Inatunga njia za kusimamia mashujaa na nguvu zao.

models.py
-Madhumuni: Inaelezea mifano ya data inayotumiwa kwenye app.
-Mifano:
  -Hero: Inawakilisha mashujaa wenye sifa kama name, super_name, na uhusiano na HeroPower.
  -Power: Inawakilisha nguvu za kipekee zenye sifa kama name na description.
  -HeroPower: Meza ya kuunganishia inayounganisha mashujaa na nguvu zao, ikiwa na sifa ya nguvu.

seed.py
-Madhumuni: Inajaza database na data ya awali.
-Kazi:
  -Inafuta rekodi zilizopo kwenye database.
  -Inajaza database na nguvu zilizowekwa awali.
  -Inajaza database na mashujaa waliowekwa awali.
  -Inachanganya nguvu na mashujaa kwa nasibu na kuziokoa.

License
Hiki mradi umesajiliwa chini ya Kent License. Angalia faili ya LICENSE kwa maelezo.



