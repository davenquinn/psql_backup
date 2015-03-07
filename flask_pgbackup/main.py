# -*- coding: utf-8 -*-

import click
from arrow import now,get
from click import style, echo, secho
from pathlib import Path
from flask import current_app

from .util import message, run

#@MigrateCommand.command
def backup():
    """ Back up database to a PostgreSQL dump file."""
    DATA_DIR = current_app.config["DATA_DIR"]
    DB_NAME = current_app.config["DB_NAME"]
    message("Backing up database...", "PostgreSQL")

    fn = now().format('YYYY-MM-DD_HH.mm.ss')+".sql"
    path = Path(DATA_DIR)/"backups"
    try:
        path.mkdir()
    except OSError:
        pass
    run("pg_dump -Fc {0} > {1}".format(DB_NAME, path/fn), shell=True)
    message(style("Success!", "green"), "PostgreSQL")

#@MigrateCommand.command
def restore():
    """ Restore database from a backup."""
    DATA_DIR = app.config["DATA_DIR"]
    DB_NAME = app.config["DB_NAME"]

    echo("Which backup do you want to restore?\n")
    path = Path(DATA_DIR)/"backups"
    backups = list(path.glob("*.sql"))
    for i,back in enumerate(backups[::-1]):
        stem = back.stem
        d = get(stem)
        st = "  ("+style(str(i),
            fg="green",
            bold=True)+") "+back.stem
        st += " - "+style(d.humanize(), fg="green")
        echo(st)
    echo("")

    def validate_number(value):
        try:
            return backups[int(value)]
            return backup
        except IndexError:
            raise click.BadParameter("Pick from the available options")
        except ValueError:
            raise click.BadParameter("Enter a number")
    try:
        backup = click.prompt("Enter a number to continue",
                value_proc=validate_number, type=int)
        click.echo("")
        click.confirm("Are you sure you want to restore the database?\n"
                      "All newer changes will be lost!", abort=True)
    except click.exceptions.Abort:
        echo("")
        echo("Aborting.")
        return

    cmd = ["pg_restore",
            "--clean",
            "-d "+DB_NAME,
            str(backup)]

    run(*cmd)
    message(style("Success!", "green"),"PostgreSQL")

