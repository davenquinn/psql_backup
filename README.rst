===============================
psql_backup
===============================

`psql_backup` provides a simple command-line interface for
backing up and restoring a PostgreSQL database *en-masse*.

Features
--------

* Backup PostgreSQL database to dump files in an arbitrary directory
* Interfaces with Flask, with or without SQLAlchemy
* Uses the `click` command line interface library for easy extensibility

Todo
----

* Add some way to prune old backups
* Back up to a remote machine
* Get rid of CLI shell access for backup
* Maybe partial backups?
