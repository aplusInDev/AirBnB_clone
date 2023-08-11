#!/usr/bin/env python3
"""This module defines a class called Place
that inherits from BaseModel and represents a place"""

from models.base_model import BaseModel


class Place(BaseModel):
    """A class that inherits from BaseModel and represents a place"""

    # A public class attribute that stores the city ID of the place
    city_id: str = ""
    # A public class attribute that stores the user ID of the place
    user_id: str = ""
    # A public class attribute that stores the name of the place
    name: str = ""
    # A public class attribute that stores the description of the place
    description: str = ""
    # A public class attribute that stores the number of rooms of the place
    number_rooms: int = 0
    # A public class attribute that stores the number of bathrooms of the place
    number_bathrooms: int = 0
    # A public class attribute that stores the maximum number of guests of
    # the place
    max_guest: int = 0
    # A public class attribute that stores the price by night of the place
    price_by_night: int = 0
    # A public class attribute that stores the latitude of the place
    latitude: float = 0.0
    # A public class attribute that stores the longitude of the place
    longitude: float = 0.0
    # A public class attribute that stores a list of amenity IDs of the place
    amenity_ids: list = []
