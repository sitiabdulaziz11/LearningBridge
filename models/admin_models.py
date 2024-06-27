from .base_model import Base, BaseClass
from sqlalchemy import Column, \
    Integer, String, ForeignKey
# import relationship
from sqlalchemy.orm import relationship

# Adminstrator model


class Administrator(BaseClass, Base):
    """ Adminstrator model that represents adminstrator's fields/attributes.
    """
    __tablename__ = "administrators"

    firstname = Column(String(50), nullable=False)
    middlename = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    phone_no = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(250), nullable=False, unique=True)
    image_file = Column(String(50), unique=True)
    address = Column(String(100), nullable=False)

    # defin the relationship

    students = relationship("Student", backref="admin")
    teachers = relationship("Teacher", backref="admin")
    parent = relationship("Parent", backref="admin")
