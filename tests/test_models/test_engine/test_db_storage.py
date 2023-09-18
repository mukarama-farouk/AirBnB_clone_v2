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
storage_type = os.environ.get('HBNB_TYPE_STORAGE')
DBStorage = None
if storage_type == "db":
    DBStorage = db_storage.DBStorage

if env_value == 'db':
    class test_DBStorage(unittest.TestCase):
        """ a class that tests the DB storage method """
        @classmethod
        def setUp(cls):
            """ Set up test environment """
            cls.db_func = inspect.getmembers(DBStorage, inspect.isfunction)

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

        def test_new(self):
            """ test case for creation of newly created instances """

        def test_all(self):
            """ test case for the proper return of all instances of a class """

        def test_save(self):
            """ test case for DBStorage save method """

        def test_delete(self):
            """ test case for DBStorage delete method """

        def test_reload(self):
            """ test case for reloading the DB storage """
