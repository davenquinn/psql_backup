# -*- coding: utf-8 -*-

import click
from arrow import now,get
from click import style, echo, secho
from pathlib import Path

from .util import message, run

class PSQL_Backup(object):
    def __init__(self, db_name, backup_dir):
        self.DB_NAME = db_name
        self.BACKUP_DIR = Path(backup_dir)

    def backup(self):
        """ Back up database to a PostgreSQL dump file."""

        message("Backing up database...")

        fn = now().format('YYYY-MM-DD_HH.mm.ss')+".sql"
        path = self.BACKUP_DIR
        try:
            path.mkdir()
        except OSError:
            pass
        run("pg_dump -Fc {0} > {1}".format(self.DB_NAME, path/fn), shell=True)
        message(style("Success!", "green"))

    def restore(self):
        """ Restore database from a backup."""

        echo("Which backup do you want to restore?\n")
        path = self.BACKUP_DIR
        backups = list(path.glob("*.sql"))
        for i,back in enumerate(backups[::-1]):
            stem = back.stem
            date = get(stem)
            st = "  ("+style(str(i),
                fg="green",
                bold=True)+") "+back.stem
            st += " - "+style(date.humanize(), fg="green")
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
            echo("Aborting backup.")
            return

        cmd = ["pg_restore",
                "--clean",
                "-d "+self.DB_NAME,
                str(backup)]

        run(*cmd)
        message(style("Success!", "green"))

