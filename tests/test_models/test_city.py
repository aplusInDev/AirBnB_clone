#!/usr/bin/python3

"""Unittest for city"""

import unittest
from datetime import datetime
from models.city import City
import models.city
import os


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def setUp(self):
        """Set up method"""
        self.city = City()
        self.city2 = City()

    def tearDown(self):
        """Tear down method"""
        del self.city
        del self.city2
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertTrue(len(models.city.__doc__) > 0)

    def test_class_docstring(self):
        """Test for the existence of BaseModel class docstring"""
        self.assertTrue(len(City.__doc__) > 0)

    def test_methods_docstring(self):
        """Test for the existence of methods docstring"""
        self.assertTrue(len(City.__init__.__doc__) > 0)
        self.assertTrue(len(City.__str__.__doc__) > 0)
        self.assertTrue(len(City.save.__doc__) > 0)
        self.assertTrue(len(City.to_dict.__doc__) > 0)

    def test_instance(self):
        """Test for correct instantiation of BaseModel"""
        self.assertIsInstance(self.city, City)

    def test_id_exists(self):
        """Test for existence of id"""
        self.assertTrue(hasattr(self.city, "id"))

    def test_unique_id(self):
        """Test for unique id"""
        self.assertNotEqual(self.city.id, self.city2.id)

    def test_created_at_exists(self):
        """Test for existence of created_at"""
        self.assertTrue(hasattr(self.city, "created_at"))

    def test_type_of_created_at(self):
        """Test for correct type of created_at"""
        self.assertIsInstance(self.city.created_at, datetime)

    def test_updated_at_exists(self):
        """Test for existence of updated_at"""
        self.assertTrue(hasattr(self.city, "updated_at"))

    def test_type_of_updated_at(self):
        """Test for correct type of updated_at"""
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_str_method(self):
        """Test for correct __str__ output"""
        self.city.name = "Holberton"
        self.city.my_number = 89
        string = "[City] ({}) {}".format(self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), string)

    def test_save_method(self):
        """Test for correct update of updated_at"""
        first_updated_at = self.city.updated_at
        self.city.save()
        second_updated_at = self.city.updated_at
        self.assertNotEqual(first_updated_at, second_updated_at)

    def test_to_dict_method(self):
        """Test for correct dictionary representation"""
        base_dict = self.city.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)
        self.assertEqual(base_dict['id'], self.city.id)
        self.assertEqual(base_dict['created_at'],
                         self.city.created_at.isoformat())
        self.assertEqual(base_dict['updated_at'],
                         self.city.updated_at.isoformat())
        self.assertEqual(base_dict['__class__'], 'City')
        self.assertEqual(self.city.__class__.__name__, 'City')

    def test_city_name(self):
        """Test for amenity name"""
        self.city.name = "Holberton"
        self.assertEqual(self.city.name, "Holberton")

    def test_city_state_id(self):
        """Test for state id"""
        self.city.state_id = "1234"
        self.assertEqual(self.city.state_id, "1234")
