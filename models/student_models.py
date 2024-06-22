from .base import Base, Column, Integer, String, ForeignKey, datetime, relationship

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
    # Define the relationship to students
    subjects = relationship("Subject", secondary=student_subject, back_populates="students")
    results = relationship("Result", back_populates="student")


