#!/usr/bin/python3
"""
This module defines a class called BaseModel that represents the base
model for all other classes in the project.
"""

from datetime import datetime
import uuid
import models


time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """This class is the base class for all other classes in this project"""

    def __init__(self, *args, **kwargs):
        """This method initializes a new instance of the BaseModel class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, time)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """This method returns a string representation of the BaseModel
        instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """This method updates the updated_at attribute with the current
        datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """This method returns a dictionary representation of the BaseModel
        instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
