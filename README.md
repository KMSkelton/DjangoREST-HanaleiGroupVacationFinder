# Get started
This is very helpful for those who would like to roll their own DRF backend: https://www.valentinog.com/blog/tutorial-api-django-rest-react/

Deployed a Postgres db to https://evening-bastion-83894.herokuapp.com/api/location/?format=json

For local development
Start a virtual environment:

`python3 -m venv VenvDjango`

If the Django server can't find a table (but this is not your first time using this), try the following:

Delete `db.sqlite3`

Make the migrations for the 'locations' app:

`python manage.py makemigrations locations`

Finally, migrate the database: 

`python manage.py migrate`
