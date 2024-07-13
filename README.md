#1. > Command for installing fastapi
==> pip install fastapi

#2. > Command for installing uvicorn web server
==> pip install uvicorn

#3. > Command for running the web development server
==> uvicorn main:app --reload

#4. > Command for installing database driver for MySQL ==> mysqlclient (optional only if you are using MySQL database)
==> pip install mysqlclient

#5. > Optional Command (chaidaina jasto lagcha) (optional only if you are using MySQL database)
==> pip install databases['mysql']

#6. > Command for installing database driver for postgresql ==> psycopg2-binary (optional only if you are using postgresql database)
==> pip install psycopg2-binary

#7. > Command for installing SQLAlchemy
==> pip install sqlalchemy

#8. > Command for installing SQLAlchemy Utils (for getting the choices list which wont be present in SQLAlchemy class or models)
==> pip install sqlalchemy_utils

#9. > Command for installing werkzeug ( package for hashing the password and checking the hashed password )
==> pip install werkzeug

#10> Command for Installing FastAPI JWT Auth
==> pip install fastapi-jwt-auth


# Command for Generating token_hex
==> python
==> now, python shell will open
==> import secrets
==> secrets.token_hex()      it will generate the token


## Command for Creating the tables in the database
==> python init_db.python
