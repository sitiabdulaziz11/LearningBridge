from .base import Base, Column, Integer, String, ForeignKey, datetime, relationship, Table
from teacher_models import student_teacher

# Student - Subject many-to-many relationship
student_subject = Table('student_subject', Base.metadata,
     Column('student_id', Integer, ForeignKey('students.id')),
     Column('subject_id', Integer, ForeignKey('subjects.id')),
)

class Student(Base):
    """ Student model that represents student's fields/attributes.
    """
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True)
    firstname = Column(String(50), nullable=False)
    middilename = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(250), nullable=False, unique=True)
    birth_date = Column(datetime, nullable=False, default=datetime.now().strftime('%d-%m-%Y')) # Q?
    image_file = Column(String(50), unique=True, default="default.jpg")
    # address = relationship("Address", backref="student", uselist=False)
    # address = Column(String(100), nullable=false)
    phone_no = Column(String(10), unique=True)
    conduct = Column(String(10), nullable=False)#Q?
    section = Column(String(10), nullable=False)#Q?
    
    # Define the relationship with other tables
    teachers = relationship("Teacher", secondary=student_teacher, back_populates="students")
    subjects = relationship("Subject", secondary=student_subject, back_populates="students")
    results = relationship("Result", back_populates="student")
    admin_id = Column(Integer, ForeignKey("administrators.id"), nullable=False)
    parent_id = Column(Integer, ForeignKey("parents.id"), nullable=False)
