===============================
Flask-PGBackup
===============================

Flask-PGBackup provides a simple command-line interface for
backing up and restoring a PostgreSQL database *en-masse*.

Flask is essentially a vehicle to store config files for
the project, and it is likely that we will abstract away
in the future.

Features
--------

* Backup PostgreSQL database to dump files in an arbitrary directory
* Interfaces with Flask, with or without SQLAlchemy
* Uses the `click` command line interface library for easy extensibility

Todo
----

* Divorce from Flask to make it a generalized toolkit
* Add some way to prune old backups
* Back up to a remote machine
* Get rid of CLI shell access for backup
* Maybe partial backups?
