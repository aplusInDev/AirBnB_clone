#!/usr/bin/env python3
"""This module defines a class called User
that inherits from BaseModel and represents a user"""

from models.base_model import BaseModel


class User(BaseModel):
    """A class that inherits from BaseModel and represents a user"""

    # A public class attribute that stores the email of the user
    email: str = ""
    # A public class attribute that stores the password of the user
    password: str = ""
    # A public class attribute that stores the first name of the user
    first_name: str = ""
    # A public class attribute that stores the last name of the user
    last_name: str = ""
