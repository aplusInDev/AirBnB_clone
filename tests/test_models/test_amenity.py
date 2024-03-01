#!/usr/bin/python3

"""Unittest for amenity"""

import unittest
from datetime import datetime
from models.amenity import Amenity
import models.amenity
import os


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def setUp(self):
        """Set up method"""
        self.amenity = Amenity()
        self.amenity2 = Amenity()

    def tearDown(self):
        """Tear down method"""
        del self.amenity
        del self.amenity2
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertTrue(len(models.amenity.__doc__) > 0)

    def test_class_docstring(self):
        """Test for the existence of BaseModel class docstring"""
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_methods_docstring(self):
        """Test for the existence of methods docstring"""
        self.assertTrue(len(Amenity.__init__.__doc__) > 0)
        self.assertTrue(len(Amenity.__str__.__doc__) > 0)
        self.assertTrue(len(Amenity.save.__doc__) > 0)
        self.assertTrue(len(Amenity.to_dict.__doc__) > 0)

    def test_instance(self):
        """Test for correct instantiation of BaseModel"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_id_exists(self):
        """Test for existence of id"""
        self.assertTrue(hasattr(self.amenity, "id"))

    def test_unique_id(self):
        """Test for unique id"""
        self.assertNotEqual(self.amenity.id, self.amenity2.id)

    def test_created_at_exists(self):
        """Test for existence of created_at"""
        self.assertTrue(hasattr(self.amenity, "created_at"))

    def test_type_of_created_at(self):
        """Test for correct type of created_at"""
        self.assertIsInstance(self.amenity.created_at, datetime)

    def test_updated_at_exists(self):
        """Test for existence of updated_at"""
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def test_type_of_updated_at(self):
        """Test for correct type of updated_at"""
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_str_method(self):
        """Test for correct __str__ output"""
        self.amenity.name = "Holberton"
        self.amenity.my_number = 89
        string = "[Amenity] ({}) {}".format(self.amenity.id,
                                            self.amenity.__dict__)
        self.assertEqual(str(self.amenity), string)

    def test_save_method(self):
        """Test for correct update of updated_at"""
        first_updated_at = self.amenity.updated_at
        self.amenity.save()
        second_updated_at = self.amenity.updated_at
        self.assertNotEqual(first_updated_at, second_updated_at)

    def test_to_dict_method(self):
        """Test for correct dictionary representation"""
        base_dict = self.amenity.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)
        self.assertEqual(base_dict['id'], self.amenity.id)
        self.assertEqual(base_dict['created_at'],
                         self.amenity.created_at.isoformat())
        self.assertEqual(base_dict['updated_at'],
                         self.amenity.updated_at.isoformat())
        self.assertEqual(base_dict['__class__'], 'Amenity')
        self.assertEqual(self.amenity.__class__.__name__, 'Amenity')

    def test_amenity_name(self):
        """Test for amenity name"""
        self.amenity.name = "Holberton"
        self.assertEqual(self.amenity.name, "Holberton")
