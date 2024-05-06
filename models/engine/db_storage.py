#!/usr/bin/python3
"""This is for the db-storage engine"""
from os import environ, getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base

class DBStorage():
    """"""

    __engine = None
    __session = None

    def __init__(self):
        """"""
        
        user = environ.get('HBNB_MYSQL_USER', 'hbnb_dev')
        password = environ.get('HBNB_MYSQL_PWD', 'hbnb_dev_pwd')
        host = environ.get('HBNB_MYSQL_HOST', 'localhost')
        database = environ.get('HBNB_MYSQL_DB', 'hbnb_dev_db')
        hbnb_env = environ.get('HBNB_ENV')

        self.__engine = create_engine(
                """mysql+mysqldb://{}:{}@{}/{}"""
                .format(user, password, host, database), pool_pre_ping=True)
        if hbnb_env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """"""

        dictionary = {}

        if cls == None:
            cls_list = [User, State, City, Amenity, Place, Review]
        else:
            cls_list = [cls]

        for cls in cls_list:
            query = self.__session.query(cls).all()
            for new_obj in query:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                dictionary[key] = new_obj
        return dictionary

    def new(self, obj):
        """"""

        self.__session.add(obj)

    def save(self):
        """"""

        self.__session.commit()

    def delete(self, obj=None):
        """"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """"""

        from models.user import User
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        Base.metadata.create_all(self.__engine)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)

        self.__session = scoped_session(Session)
