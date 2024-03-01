#!/usr/bin/python3
"""This module contains the Review class for the AirBnB clone"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
