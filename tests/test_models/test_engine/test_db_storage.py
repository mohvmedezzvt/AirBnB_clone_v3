#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_get_invalid_class(self):
        """Test get with an invalid class"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        retrieved_obj = self.storage.get("InvalidClass", obj.id)
        self.assertIsNone(retrieved_obj)

    def test_get_invalid_class_and_id(self):
        """Test get with an invalid class and ID"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        retrieved_obj = self.storage.get("InvalidClass", "invalid_id")
        self.assertIsNone(retrieved_obj)

    def test_count_empty_storage(self):
        """Test count with an empty storage"""
        count = self.storage.count()
        self.assertEqual(count, 0)

    def test_count_specific_class_empty_storage(self):
        """Test count with an empty storage and specifying a class"""
        count = self.storage.count("State")
        self.assertEqual(count, 0)

    def test_get_nonexistent_object(self):
        """Test get with a nonexistent object"""
        obj_id = "nonexistent_id"
        retrieved_obj = self.storage.get("BaseModel", obj_id)
        self.assertIsNone(retrieved_obj)

    def test_count_specific_class_nonexistent_objects(self):
        """Test count with specifying a class and nonexistent objects"""
        count = self.storage.count("State")
        self.assertEqual(count, 0)
