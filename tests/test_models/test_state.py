#!/usr/bin/python3

"""Unittest for state"""

import unittest
from datetime import datetime
from models.state import State
import models.state
import os


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def setUp(self):
        """Set up method"""
        self.state = State()
        self.state2 = State()

    def tearDown(self):
        """Tear down method"""
        del self.state
        del self.state2
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertTrue(len(models.state.__doc__) > 0)

    def test_class_docstring(self):
        """Test for the existence of BaseModel class docstring"""
        self.assertTrue(len(State.__doc__) > 0)

    def test_methods_docstring(self):
        """Test for the existence of methods docstring"""
        self.assertTrue(len(State.__init__.__doc__) > 0)
        self.assertTrue(len(State.__str__.__doc__) > 0)
        self.assertTrue(len(State.save.__doc__) > 0)
        self.assertTrue(len(State.to_dict.__doc__) > 0)

    def test_instance(self):
        """Test for correct instantiation of BaseModel"""
        self.assertIsInstance(self.state, State)

    def test_id_exists(self):
        """Test for existence of id"""
        self.assertTrue(hasattr(self.state, "id"))

    def test_unique_id(self):
        """Test for unique id"""
        self.assertNotEqual(self.state.id, self.state2.id)

    def test_created_at_exists(self):
        """Test for existence of created_at"""
        self.assertTrue(hasattr(self.state, "created_at"))

    def test_type_of_created_at(self):
        """Test for correct type of created_at"""
        self.assertIsInstance(self.state.created_at, datetime)

    def test_updated_at_exists(self):
        """Test for existence of updated_at"""
        self.assertTrue(hasattr(self.state, "updated_at"))

    def test_type_of_updated_at(self):
        """Test for correct type of updated_at"""
        self.assertIsInstance(self.state.updated_at, datetime)

    def test_str_method(self):
        """Test for correct __str__ output"""
        self.state.name = "Holberton"
        self.state.my_number = 89
        string = "[State] ({}) {}".format(self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), string)

    def test_save_method(self):
        """Test for correct update of updated_at"""
        first_updated_at = self.state.updated_at
        self.state.save()
        second_updated_at = self.state.updated_at
        self.assertNotEqual(first_updated_at, second_updated_at)

    def test_to_dict_method(self):
        """Test for correct dictionary representation"""
        base_dict = self.state.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)
        self.assertEqual(base_dict['id'], self.state.id)
        self.assertEqual(base_dict['created_at'],
                         self.state.created_at.isoformat())
        self.assertEqual(base_dict['updated_at'],
                         self.state.updated_at.isoformat())
        self.assertEqual(base_dict['__class__'], 'State')
        self.assertEqual(self.state.__class__.__name__, 'State')

    def test_state_name(self):
        """Test for amenity name"""
        self.state.name = "Holberton"
        self.assertEqual(self.state.name, "Holberton")
