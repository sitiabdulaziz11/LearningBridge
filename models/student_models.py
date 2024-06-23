from sqlalchemy import Column, String, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .teacher_models import student_teacher
from .base_model import Base, BaseClass
# Student - Subject many-to-many relationship
student_subject = Table('student_subject', Base.metadata,
                        Column('student_id', String(20),
                               ForeignKey('students.id')),
                        Column('subject_id', String(20),
                               ForeignKey('subjects.id')),
                        )


class Student(BaseClass, Base):
    """ Student model that represents student's fields/attributes.
    """
    __tablename__ = "students"

    firstname = Column(String(50), nullable=False)
    middilename = Column(String(50), nullable=True)
    lastname = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(250), nullable=False, unique=True)
    birth_date = Column(DateTime, nullable=False,
                        default=datetime.now().strftime('%d-%m-%Y'))  # Q?
    image_file = Column(String(50), unique=True, default="default.jpg")
    # address = relationship("Address", backref="student", uselist=False)
    # address = Column(String(100), nullable=false)
    phone_no = Column(String(10), unique=True)
    conduct = Column(String(10), nullable=True)  # Q?
    section = Column(String(10), nullable=True)  # Q?

    results = relationship("Result", back_populates="student")
    # Define the relationship with other tables
    teachers = relationship(
        "Teacher", secondary=student_teacher, back_populates="students")
    subjects = relationship(
        "Subject", secondary=student_subject, back_populates="students")
    admin_id = Column(String(20), ForeignKey(
        "administrators.id"), nullable=True)
    parent_id = Column(String(20), ForeignKey("parents.id"), nullable=True)
