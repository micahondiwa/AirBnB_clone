#!/usr/bin/python3
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """The City class representation"""
    if models.storage_t = "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('state.id'), nullable=False)
        name = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kargs):
        """Initializes city"""
        super().__init__(*args, **kargs)
