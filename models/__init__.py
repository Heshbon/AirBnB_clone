#!/usr/bin/python3
"""Init the package component"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
