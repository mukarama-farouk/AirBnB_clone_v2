#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

import os
env_value = os.environ.get('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    if env_value == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state')
    else:
        name = ""

        @property
        def cities(self):
            from models.__init__ import storage
            obj_list = []
            strg = storage.all(City)
            for value in strg:
                if self.id == value.state_id:
                    obj_list.append(value)
            return obj_list
