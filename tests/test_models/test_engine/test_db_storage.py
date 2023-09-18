#!/usr/bin/python3
""" Module for testing DB storage"""

from models import storage
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import inspect
import os
import unittest

env_value = os.environ.get('HBNB_TYPE_STORAGE')
known_classes = {"Amenity": Amenity, "City": City, "Place": Place,
                 "Review": Review, "State": State, "User": User}

user = os.environ.get('HBNB_MYSQL_USER')
pwd = os.environ.get('HBNB_MYSQL_PWD')
host = os.environ.get('HBNB_MYSQL_HOST')
database = os.environ.get('HBNB_MYSQL_DB')
env = os.environ.get('HBNB_ENV')

DBStorage = None
if env_value == "db":
    DBStorage = db_storage.DBStorage

if env_value == 'db':
    class test_DBStorage(unittest.TestCase):
        """ a class that tests the DB storage method """
        def setUp(self):
            """ Set up test environment """
            self.db_func = inspect.getmembers(DBStorage, inspect.isfunction)
            self.engine = create_engine(f"mysql+mysqldb://{user}"
                                        ":{pwd}@{host}/{database}",
                                        pool_pre_ping=True)
            self.Session = sessionmaker(bind=self.engine)

        def test_docstring(self):
            """Test for the DBStorage class docstring"""
            if not DBStorage:
                return
            self.assertIsNot(DBStorage.__doc__, None)
            self.assertTrue(len(DBStorage.__doc__) >= 1,
                            "DBStorage class needs a docstring")

        def test_methods_docstrings(self):
            """Test for the presence of docstrings in DBStorage methods"""
            for func in self.db_func:
                self.assertIsNot(func[1].__doc__, None,
                                 "{:s} method needs a docstring".format(func[0]))
                self.assertTrue(len(func[1].__doc__) >= 1,
                                "{:s} method needs a docstring".format(func[0]))

        def test_module_docstring(self):
            """Test for the db_storage.py module docstring"""
            self.assertIsNot(db_storage.__doc__, None,
                             "db_storage.py needs a docstring")
            self.assertTrue(len(db_storage.__doc__) >= 1,
                            "db_storage.py needs a docstring")

        def tearDown(self):
            """ Remove storage file at end of tests """
            """cleanup actions go here"""
            self.engine.dispose()

        def test_new(self):
            """ test case for creation of newly created instances """
            session = self.Session()
            new_user = User()
            new_user.email = "mail@google.com"
            new_user.password = "googlepassw0rd"
            new_user.first_name = "hazel"
            new_user.last_name = "hasbi"
            new_review = Review(text="good place to stay", place_id="x5050", user_id="x05")
            new_places = Place(city_id="x5050", user_id="b40",
                                    name="johannesburg",
                                    description="the capital of SA",
                                    number_rooms=5, max_guest=9,
                                    price_by_night=100, latitude=12.0,
                                    longitude=15.5)
            new_places.reviews.append(new_review)
            new_user.places.append(new_places)
            new_user.reviews.append(new_review)
            session.add(new_user)
            session.commit()
            session.close()

            session = self.Session()
            res_user = session.query(User).filter(User.first_name == "hazel").first()
            session.close()

            self.assertIsNotNone(res_user)
            self.assertEqual(res_user.first_name, "hazel")
            self.assertIsNotNone(res_user.places)
            self.assertEqual(res_user.places.reviews, new_review)

        def test_all(self):
            """ test case for the proper return of all instances of a class """

        def test_save(self):
            """ test case for DBStorage save method """

        def test_delete(self):
            """ test case for DBStorage delete method """

        def test_reload(self):
            """ test case for reloading the DB storage """
