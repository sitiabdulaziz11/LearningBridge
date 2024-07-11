from .base_model import Base, BaseClass
from sqlalchemy import Column, Integer, String, ForeignKey
from datetime import datetime
from sqlalchemy import DateTime

# import relationship
from sqlalchemy.orm import relationship
from flask_login import UserMixin

# Adminstrator model


class Administrator(BaseClass, Base, UserMixin):
    """Adminstrator model that represents adminstrator's fields/attributes."""

    __tablename__ = "administrators"

    firstname = Column(String(50), nullable=False)
    middlename = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    phone_no = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    gender = Column(String(20), nullable=False)
    hire_date = Column(
        DateTime, nullable=False, default=datetime.now().strftime("%d-%m-%Y")
    )
    image_file = Column(String(50), nullable=False, default='default.jpg')
    address = Column(String(300))
    age = Column(Integer, nullable=False)

    # define relationships

    students = relationship("Student", backref="admin")
    teachers = relationship("Teacher", backref="admin")
    parent = relationship("Parent", backref="admin")
