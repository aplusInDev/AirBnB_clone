#!/usr/bin/env python3
"""This module defines a class called Review
that inherits from BaseModel and represents a review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """A class that inherits from BaseModel and represents a review"""

    # A public class attribute that stores the place ID of the review
    place_id: str = ""
    # A public class attribute that stores the user ID of the review
    user_id: str = ""
    # A public class attribute that stores the text of the review
    text: str = ""
