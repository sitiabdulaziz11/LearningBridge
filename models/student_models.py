from sqlalchemy import Column, String, Integer, ForeignKey, Table, Date
from sqlalchemy.orm import relationship
from datetime import datetime
from .teacher_models import students_teachers
from .base_model import Base, BaseClass
from flask_login import UserMixin


# Student - Subject many-to-many relationship
student_subject = Table(
    "student_subject",
    Base.metadata,
    Column("student_id", String(20), ForeignKey("students.id")),
    Column("subject_id", String(20), ForeignKey("subjects.id")),
)


class Student(BaseClass, Base, UserMixin):
    """Student model that represents student's fields/attributes."""

    __tablename__ = "students"

    firstname = Column(String(50), nullable=False)
    middlename = Column(String(50), nullable=True)
    lastname = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(250), nullable=False, unique=True)
    birth_date = Column(Date, nullable=False) # Q?
    age = Column(Integer, nullable=False)
    image_file = Column(String(50), unique=True)
    gender = Column(String(20), nullable=False)
    # address = relationship("Address", backref="student", uselist=False)
    address = Column(String(100), nullable=False)
    phone_no = Column(String(60), unique=True)
    # conduct = Column(String(60), nullable=True)  # Q?
    grade = Column(String(60), nullable=False)
    section = Column(String(60), nullable=True)  # Q?
    
    # Define the relationship with other tables
    results = relationship("Result", back_populates="student")
    teachers = relationship(
        "Teacher", secondary=students_teachers, back_populates="students"
    )
    subjects = relationship(
        "Subject", secondary=student_subject, back_populates="students"
    )
    admin_id = Column(String(60), ForeignKey("administrators.id"), nullable=True)
    parent_id = Column(String(60), ForeignKey("parents.id"), nullable=True)
