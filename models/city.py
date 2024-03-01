#!/usr/bin/python3
"""This module contains the City class for the AirBnB clone"""
from models.base_model import BaseModel


class City(BaseModel):
    """This class inherits from BaseModel"""
    state_id = ""
    name = ""
