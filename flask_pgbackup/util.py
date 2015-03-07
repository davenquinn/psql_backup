# -*- coding: utf-8 -*-

from click import echo, style
from subprocess import call
from shlex import split

def message(message, section=None, color="cyan"):
    s = "["+style(section, color)+"] " if section else ""
    s += message
    echo(s)

def run(*command, **kwargs):
    shell = kwargs.pop("shell",False)
    command = " ".join(command)
    echo("➔ "+style(command,"green"))
    if shell:
        call(command,shell=True)
    else:
        call(split(command))


