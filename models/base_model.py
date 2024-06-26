#!/usr/bin/env python3
"""This module defines the base class and all the neccesary function """

from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid

Base = declarative_base()

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseClass:
    """Base class"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, **kwargs):
        """Initialize the base model class """
        if kwargs:
            """Set the attribute of the base model"""
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at\
            ", None) and isinstance(kwargs["created_at"], str):
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at\
            ", None) and isinstance(kwargs["updated_at"], str):
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def __str__(self):
        """Function used for representation of the baseModel class"""
        return "[{}] ({}) {}\
".format(self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        """Function to convert and object to a dictionary"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)

        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" and "password" in new_dict:
            del new_dict["password"]
            del new_dict["_sa_instance_state"]
            return new_dict

    def save(self):
        """Function to save the object"""
        self.updated_at = datetime.utcnow()
        from models import storage
        storage.new(self)
        storage.save()

    def delete(self):
        """Deletes the current instalnce from the storage"""
        from models import storage
        storage.delete(self)
        storage.save()
