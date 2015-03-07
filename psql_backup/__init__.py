# -*- coding: utf-8 -*-

__author__ = 'Daven Quinn'
__email__ = 'dev@davenquinn.com'
__version__ = '0.1.0'

from functools import partial
from .commands import backup, restore

def prepare_commands(DB_NAME, BACKUP_DIR):
    """ Prepare backup and restore commands for inclusion in an application.
    """
    return dict(
        backup=partial(backup, DB_NAME, BACKUP_DIR),
        restore=partial(restore, DB_NAME, BACKUP_DIR))
