#!/usr/bin/env python3
"""This claass defines the database storage engine for the
immunization tracking system"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.admin_models import Administrator
from models.student_models import Student
from models.term import Term
from models.parent_models import Parent
from models.subject_models import Subject
from models.result_models import Result
from models.teacher_models import Teacher
from models.sub_result_models import SubjectResult as SubResult

classes = {
    Administrator.__name__: Administrator,
    Student.__name__: Student,
    Term.__name__: Term,
    SubResult.__name__: SubResult,
    Parent.__name__: Parent,
    Subject.__name__: Subject,
    Result.__name__: Result,
    Teacher.__name__: Teacher
}

class DBStorage:
    def __init__(self):
        """Initialize the data storage class"""
        LB_USER = os.getenv("LB_USER", "lb")
        LB_PWD = os.getenv("LB_PWD", "Team_Project")
        LB_HOST = os.getenv("LB_HOST", "localhost")
        LB_DB = os.getenv("LB_DB", "LB")
        ENV = os.getenv("ENV",  "development")

        if ENV == 'production':
            self.__engine = create_engine(
                "postgresql://{}:{}@{}/{}".format(
                    LB_USER, LB_PWD, LB_HOST, LB_DB
                ),
                pool_pre_ping=True,
            )
        elif ENV == 'development':
            self.__engine = create_engine(
                "mysql+mysqldb://{}:{}@{}/{}".format(
                    LB_USER, LB_PWD, LB_HOST, LB_DB
                ),
                pool_pre_ping=True,
            )
        else:
            self.__engine = create_engine(
                "sqlite:///{}".format(LB_DB),
                pool_pre_ping=True,
            )
        # drop all tables if the TUTORPLAN_ENV is "test"
        if os.getenv("LearningBridge_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + "." + obj.id
                    new_dict[key] = obj
        return new_dict

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def new(self, obj):
        """add the object to the current database sesson"""
        self.__session.add(obj)

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """closes the session"""
        self.__session.remove()

    def get(self, cls, id):
        """get an object from the database"""
        if cls is not None and id is not None:
            obj = self.__session.query(cls).get(id)
            return obj
        return None

    # get object by email
    def get_by_email(self, cls, email):
        """get an object from the database"""
        if cls is not None and email is not None:
            obj = self.__session.query(cls).filter_by(email=email).first()
            return obj
        return None
