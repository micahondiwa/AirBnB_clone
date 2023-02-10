#!/usr/bin/python3
"""Defines all common attributes and methods
for other classes (City, Place, Review, State, and User)"""


import uuid
from datetime import datetime


class BaseModel:
    """Class that defines the Base Class"""

    def __init__(self):
        """Method that initializes the instance
        Args:
        id: string - assign with an uuid when an
        instance is created
        created_at: datetime - assign with the current
        datetime when an instance is
        created
        updated_at: datetime - assign with the current
        datetime when an instance is
        created and it will be
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        @property
        def __str__(self):
            return "[{}] ({}) {}".format(self.__class__.__name__,
                                         self.id, self.__dict__)

        @property
        def save(self):
            self.updated_at = datetime.now()
            return self.updated_at

        @property
        def to_dict(self):
            __dict__ = self.__dict__.copy()
            __dict__["__class__"] = self.__class__.__name__
            __dict__["created_at"] = self.created_at.isoformat()
            __dict__["updated_at"] = self.updated_at.isoformat()
            return __dict__
