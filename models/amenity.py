#!/usr/bin/python3
"""
Holds the Amenity class
"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    A class representing the amenities
    """
    if models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

        def __init__(self, *args, **kwargs):
            """
            Initializing amenity
            """
            super().__init__(*args, **kwargs)
