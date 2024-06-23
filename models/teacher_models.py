from .base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, datetime, relationship, Table


# Parent - Teacher many-to-many relationship
student_teacher = Table('student_teacher', Base.metadata,
                        Column('student_id', Integer,
                               ForeignKey('students.id')),
                        Column('teacher_id', Integer,
                               ForeignKey('teachers.id')),
                        )


class Teacher(Base):
    """ Teacher model that represents teacher's fields/attributes.
    """
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True)
    firstname = Column(String(50), nullable=False)
    middlename = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(250), nullable=False, unique=True)
    hire_date = Column(datetime, nullable=False,
                       default=datetime.now().strftime('%d-%m-%Y'))  # Q?
    image_file = Column(String(50), nullable=False,
                        unique=True, default="default.jpg")
    # address = relationship("Address", ?backref="teacher", uselist=False)?
    # address = Column(String(100), nullable=false)
    phone_no = Column(String(10), nullable=False, unique=True)
    # subject = Column(String(150), nullable=False) # Q?what subject does teacher teach?
    # Q? what section does teacher teach?
    section = Column(String(150), nullable=False)

    # define the relationship
    parents = relationship(
        "Parent", secondary="parent_teacher", back_populates="teachers")
    admin_id = Column(Integer, ForeignKey("administrators.id"), nullable=False)
    results = relationship("Result", back_populates="teacher")
    subjects = relationship("Subject", back_populates="teacher")
    students = relationship(
        "Student", secondary=student_teacher, back_populates="teachers")
