#!/usr/bin/python3
""" Module for testing DB storage"""
import unittest
from models.base_model import BaseModel
from models import storage

import os
env_value = os.environ.get('HBNB_TYPE_STORAGE')

if env_value == 'db':

    class test_DBStorage(unittest.TestCase):
        """ a class that to test the DB storage method """

        def setUp(self):
            """ Set up test environment """

        def tearDown(self):
            """ Remove storage file at end of tests """
            """cleanup actions go here"""

        def test_new(self):
            """ test case for creation of newly created instances """

        def test_all(self):
            """ test case for the proper return of all instances of a class """

        def test_save(self):
            """ test case for DBStorage save method """

        def test_reload(self):
            """ test case for reloading the DB storage """
