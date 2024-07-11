from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime
from .base_model import Base, BaseClass
from datetime import datetime
from sqlalchemy.orm import relationship
from flask_login import UserMixin

# Parent - Teacher many-to-many relationship
students_teachers = Table(
    "students_teachers",
    Base.metadata,
    Column("student_id", String(20), ForeignKey("students.id")),
    Column("teacher_id", String(20), ForeignKey("teachers.id")),
)


class Teacher(BaseClass, Base, UserMixin):
    """Teacher model that represents teacher's fields/attributes."""

    __tablename__ = "teachers"

    firstname = Column(String(50), nullable=False)
    middlename = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(250), nullable=False, unique=True)
    phone_no = Column(String(10), nullable=False, unique=True)
    gender = Column(String(20), nullable=False)
    hire_date = Column(
        DateTime, nullable=False, default=datetime.now().strftime("%d-%m-%Y")
    )  # Q?
    age = Column(Integer, nullable=False)
    image_file = Column(String(50), nullable=False, unique=True, default="default.jpg")
    address = Column(String(100), nullable=False)
    grade = Column(String(60), nullable=False)
    section = Column(String(150), nullable=True)
    # subject = Column(String(150),
    # nullable=False) # Q?what subject does teacher teach?
    # Q? what section does teacher teach?
    
    # define the relationship
    parents = relationship(
        "Parent", secondary="parent_teacher", back_populates="teachers"
    )
    admin_id = Column(String(20), ForeignKey("administrators.id"), nullable=False)
    results = relationship("Result", back_populates="teacher")
    subjects = relationship("Subject", back_populates="teacher")
    students = relationship(
        "Student", secondary=students_teachers, back_populates="teachers"
    )
