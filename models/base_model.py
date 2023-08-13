#!/usr/bin/python3
"""This module defines a class called BaseModel that represents the base
model for all other classes in the project."""

import uuid
import datetime
import models


class BaseModel():
    """This class defines the attributes and methods for
    the base model of the project."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """This method initializes a new instance of the BaseModel class.

        Args:
            *args: Arbitrary arguments that are ignored.
            **kwargs: Arbitrary keyword arguments that are
                assigned to the instance attributes.

        Attributes:
            id: A unique string identifier for the instance.
            created_at: A datetime object that represents
                the creation time of the instance.
            updated_at: A datetime object that represents
                the last update time of the instance."""

        if not kwargs:
            self.id: str = str(uuid.uuid4())
            self.created_at: datetime.datetime = datetime.datetime.now()
            self.updated_at: datetime.datetime = datetime.datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == '__class__':
                    pass
                elif key in ['updated_at', 'created_at']:
                    f = '%Y-%m-%dT%H:%M:%S.%f'
                    setattr(self, key, datetime.datetime.strptime(value, f))
                else:
                    setattr(self, key, value)

    def __str__(self) -> str:
        """This method returns a string representation of the instance.

        Returns:
            A formatted string with the class name, the id,
            and the dictionary of the instance."""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """This method updates the updated_at attribute with the current
        datetime and saves the instance to the storage."""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self) -> dict:
        """This method returns a dictionary representation of
        the instance with all its attributes.

        Returns:
            A dictionary with all the instance attributes,
            including a key called __class__ with the class
            name as its value, and updated_at and created_at
            attributes converted from datetime objects to strings."""
        my_dict = {}
        my_dict.update(self.__dict__)
        my_dict.update({type(self).__name__})
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['created_at'] = self.created_at.isoformat()
        return my_dict
