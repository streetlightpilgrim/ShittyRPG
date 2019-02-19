# ShittyRPG
my shit rpg
this is a shitty rpg
You can now fight 2 goblins back to back

# Requirements & setup

This will install all requirements, and set up the database.

```
  $ pip install ./requirements.txt
  $ python manage.py migrate
```

# Set up admin user

Use this to log into the admin interface

```
  $ python manage.py createsuperuser
```

# Run the admin server

```
  $ python manage.py runserver
```

Access it on you browser at `http://localhost:8000/admin`

# Run the game

```
  $ python run_game.py
```
