#!/usr/bin/python3
"""
The BaseModel
"""

from datetime import datetime
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid
import hashlib

time = "%Y-%m-%dT%H:%M:%S.%f"

if models.storage_t == "db":
    Base = declarative_base()
else:
    Base = object

    class BaseModel:
        """
        The BaseModel where other classes are derived
        """
        if models.storage_t == "db":
            id = Column(String(60), primary_key=True)
            created_at = Column(DateTime, default=datetime.utcnow)
            updated_at = Column(DateTime, default=datetime.utcnow)

            def __init__(self, *args, **kwargs):
                """
                Initializing the base model
                """
                if kwargs:
                    for key, value in kwargs.items():
                        if key != "__class__":
                            setattr(self, key, value)
                    if kwargs.get("created_at", None) and
                    type(self.created_at) is str:
                        self.created_at = datetime.strptime
                        (kwargs["created_at"], time)
                    else:
                         self.created_at = datetime.now()
                    if kwargs.get("updated_at", None) and type(self.updated_at) is str):
                         self.updated_at = datetime.strptime(kwargs["updated_at"], time)
                     else:
                         self.updated_at = datetime.now()
                     if kwargs.get("id", None) is None:
                         self.id = str(uuid.uuid4())
                     else:
                         self.id = str(uuid.uuid4())
                         self.created_at = datetime.now()
                         self.updated_at = self.created_at

            def __str__(self):
                """
                String represenatation of the BaseModel class
                """
                return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

            def save(self):
                """
                Updates 'updated_at' attribute to current datetime
                """
                self.updated_at = datetime.utcnow()
                models.storage.new(self)
                models.storage.save()

                def to_dict(self, dump=None):
                    """
                    Returns key-value pairs of the instances
                    """
                    new_dict = self.__dict__.copy()
                    if "created_at" in new_dict:
                        new_dict["created_at"] = new_dict["updated_at"].strftime(time)
                    new_dict["__class__"] = self.__class__.__name__
                    if "_sa_instance_stae" in new_dict:
                        del new_dict["_sa_instance_state"]
                    if getenv("HBNB_TYPE_STORAGE") == "db":
                        if 'password' in new_dict:
                            del new_dict["password"]
                        return new_dict
                def delete(self):
                    """
                    Deleting the current instance from the storage.
                    """
                    models.storage.delete(self)
