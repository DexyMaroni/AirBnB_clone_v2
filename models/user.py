#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base

class User(BaseModel):
    """This class deals with the personal details of a user"""
    __tablename__ = 'users'
    email = Column(String(128), nullable =False)
    password = Column(String(128), nullable =False)
    first_name = Column(String(123))
    last_name = Column((123)

