#!/usr/bin/python3
"""This module defines the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
