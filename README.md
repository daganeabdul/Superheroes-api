Superheroes API

Owner: Abdirahman Takhal  
Project Type: Flask RESTful API  
Status: Completed  



Description

The  Superheroes API  is a Flask backend application for tracking superheroes and their superpowers.  
It allows users to:

       View all heroes or a single hero with their powers  
       View all powers or a single power  
       Update a power's description  
       Assign powers to heroes with a strength rating  

This API is built using  Flask,  Flask-SQLAlchemy, and  Flask-Migrate  for database management.



Features

   Hero Management: View all heroes and their superhero names.  
   Power Management: View, retrieve, and update powers.  
   Hero-Power Association: Assign powers to heroes with a strength value (`Strong`, `Average`, `Weak`).  
-  Validation:  Ensures descriptions are at least 20 characters, and strengths are valid.  
-  JSON Responses: All endpoints return structured JSON data.  

Setup Instructions

1. Clone the repository

```bash
git clone https://github.com/daganeabdul/Superheroes-api.git
cd Superheroes-api
```
2. Create a virtual environment and activate it
  Mac/Linux
python3 -m venv .venv
source .venv/bin/activate

  Windows
python -m venv .venv
.venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Set environment variables
   Mac/Linux
           export FLASK_APP=app.py

 Windows
           set FLASK_APP=app.py

5. Initialize the database
flask db init   
flask db migrate -m "initial"
flask db upgrade

6. Seed the database
python seed.py

7. Run the server
flask run

By default, the server runs at: http://127.0.0.1:5000

API Endpoints
Heroes
Method
Endpoint
Description
GET
/heroes
List all heroes
GET
/heroes/<id>
Retrieve a single hero with their powers

Powers
Method
Endpoint
Description
GET
/powers
List all powers
GET
/powers/<id>
Retrieve a single power
PATCH
/powers/<id>
Update a power's description

Hero Powers
Method
Endpoint
Description
POST
/hero_powers
Assign a power to a hero with a strength value

Sample JSON for POST /hero_powers:
{
  "strength": "Average",
  "power_id": 1,
  "hero_id": 3
}


Testing
Import the provided Postman collection challenge-2-superheroes.postman_collection.json
Update the Postman environment variable base_url to your server URL (http://127.0.0.1:5000 or the port you are using)
Test all endpoints according to the collection

Technologies Used
Python 3.8+
Flask
Flask-SQLAlchemy
Flask-Migrate
SQLite (default database, can be changed)
Postman (for testing API endpoints)

