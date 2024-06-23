#!/usr/bin/python3
"""This module defines a class to manage file storage"""

from models.engine.dbStorage import DBStorage


storage = DBStorage()

storage.reload()
