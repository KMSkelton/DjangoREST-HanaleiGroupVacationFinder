# Get started
This is very helpful: https://www.valentinog.com/blog/tutorial-api-django-rest-react/

Start a virtual environment:

`python3 -m venv VenvDjango`

If the Django server can't find a table, try the following:

Delete `db.sqlite3`

Make the migrations for the 'locations' app:

`python manage.py makemigrations locations`

Finally, migrate the database: 

`python manage.py migrate`