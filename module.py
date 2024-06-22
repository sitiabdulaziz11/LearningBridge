from sqlalchemy import create_engine, Column, Integer, float, String, ForeignKey, datetime, Table #Q?
from sqlalchemy.exe.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
# from datetime import datetime Q?

# Define the database URL (SQLite in this case)
DATABASE_URL = "sqlite:///school.db"

# Create an engine
engine = create_engine(DATABASE_URL)

# Base class for models
Base = declarative_base() 


student_subject = Table('student_subject', Base.metadata,
     Column('student_id', Integer, ForeignKey('students.id')),
     Column('subject_id', Integer, ForeignKey('subjects.id')),
)

Parent_teacher = Table('parent_teacher', Base.metadata,
    Column('parent_id', Integer, ForeignKey('parents.id')),
    Column('teacher_id', Integer, ForeignKey('teachers.id')),
)

student_teacher = Table('student_teacher', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('teacher_id', Integer, ForeignKey('teachers.id')),
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
    hire_date = Column(datetime, nullable=False, default=datetime.now().strftime('%d-%m-%Y')) # Q?
    image_file = Column(String(50), nullable=False, unique=True, default="default.jpg")
    # address = relationship("Address", ?backref="teacher", uselist=False)?
    # address = Column(String(100), nullable=false)
    phone_no = Column(String(10), nullable=False, unique=True)
    subject = Column(String(150), nullable=False)#Q?what subject does teacher teach?
    section = Column(String(150), nullable=False)#Q? what section does teacher teach?


class Adminstrator(Base):
    """ Adminstrator model that represents adminstrator's fields/attributes.
    """
    __tablename__ = "administrators"
    
    id = Column(Integer, primary_key=True)
    firstname = Column(String(50), nullable=False)
    middlename = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    phone_no = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(250), nullable=False, unique=True)
    image_file = Column(String(50), nullable=False, unique=True, default="default.jpg")
    Address = Column(String(100), nullable=False)


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
    image_file = Column(String(50), nullable=False, unique=True, default="default.jpg")
    Address = Column(String(100), nullable=False)

    
# class Address(Base): is it required?
#     """ Address model that represents address fields/attributes.
#     """
#     __tablename__ = "addresses"
    
#     id = Column(Integer, primary_key=True)
#     student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
#     teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=False)
#     address = Column(String(100), nullable=False)
#     city = Column(String(100))
#     state = Column(String(100))
#     country = Column(String(100))


class Subject(Base):
    """ Subject model that represents subject's fields/attributes.
    """
    __tablename__ = "subjects"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    # Define the relationship to students
    students = relationship("Student", secondary=student_subject, back_populates="subjects")

# class ClassorSection(Base):#Q?
#     """ Section model that represents section's fields/attributes.
#     """
#     __tablename__ = "sections"
    
#     id = Column(Integer, primary_key=True)
#     secname = Column(String(100), nullable=False, unique=True)
#Assisgnment_id = relationship("Assisgnment", back_populates="term")


class Result(Base):
    """ Result model that represents result's fields/attributes.
    """
    __tablename__ = "results"
    
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False) # Each result is linked to one student or for specific student
    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=False) # who is the teacher or home room teacher
    # subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    # score = Column(Integer, nullable=False)
    overall_rank = Column(Integer, nullable=True)
    overall_average = Column(float, nullable=True)
    date = Column(datetime, nullable=False, default=datetime.now().strftime('%d-%m-%Y'))
    student = relationship("Student", back_populates="results")
    

class Term(Base):
    """ Term model that represents term's fields/attributes.
    """
    __tablename__ = "terms"
    
    id = Column(Integer, primary_key=True)
    Termname = Column(String(100), nullable=False, unique=True) # e.g., "Term 1", "Term 2"
    


class SubjectResultorAssisgnment(Base):
    """ Term model that represents term's fields/attributes.
    """
    __tablename__ = "assigments"
    
    id = Column(Integer, primary_key=True)
    test1_score = Column(float(20), nullable=False)
    test2_score = Column(float(20), nullable=False)
    test3_score = Column(float(20))
    assisgnment = Column(float(20), nullable=False)
    worksheer = Column(float(20))
    mid_exam = Column(float(20), nullable=False)
    exer_book = Column(float(20))
    final_exam = Column(float(20), nullable=False)
    # term = Column(Integer, ForeignKey("terms.id"), nullable=False)
    # rank = Column(Integer)
    # average = Column(Float)
    
    