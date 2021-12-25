# Finances
TODO: find a better name xD


# Description
Project I made to control my own finances and also study React and FastAPI.

## The Road so Far
I'm still finishing the structure. So far I have integration with SQLAlchemy, Alembic, React and some basic installation scripts but no real feature yet.

# How to Install
 - Create a user 'project' with password 'project' on postgres and a database called 'finances'. (TODO: make the database more secure)

**ATTENTION:** you must create the user and the database before running the installation script, because the script will create the tables in the database.

```
$ ./install
```

# How to Run
```
$ ./run_backend.sh
$ ./run_frontend.sh
```

**PS:** Since my main goal here is to study React and FastAPI, I made the scripts as simple as possible.

# Database Migrations

The database migrations are managed with Alembic. You can run alembic to create new migrations, upgrade/downgrade the database, etc by using a script from this project that sets the path to the config file for you:

```
$ ./scripts/alembic.sh revision "XXX - My new migration"
$ ./scripts/alembic.sh upgrade head
... you can use any alembic options has ...
```

