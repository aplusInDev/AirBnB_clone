#!/usr/bin/python3
"""This module contains the User class for the AirBnB clone"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
