from .base import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Table, relationship

# Parent - Teacher many-to-many relationship

Parent_teacher = Table('parent_teacher', Base.metadata,
                       Column('parent_id', Integer, ForeignKey('parents.id')),
                       Column('teacher_id', Integer,
                              ForeignKey('teachers.id')),
                       )


class Parent(Base):
    """ Student's Parent Module
    """
    __tabelname__ = "parents"

    id = Column(Integer, primary_key=True)
    firstname = Column(String(50), nullable=False)
    middlename = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    phone_no = Column(String(10), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(250), nullable=False, unique=True)
    image_file = Column(String(50), nullable=False,
                        unique=True, default="default.jpg")
    Address = Column(String(100), nullable=False)

    # define relation
    teachers = relationship(
        "Teacher", secondary=Parent_teacher, back_populates="parents")
    students = relationship("Student", backref="parent")

    # define relation with Administrator model
    admin_id = Column(Integer, ForeignKey("administrators.id"), nullable=False)
