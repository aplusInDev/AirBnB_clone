#!/usr/bin/python3

"""Unittest for base_model"""

import unittest
from models.base_model import BaseModel
import models.base_model
from datetime import datetime
import os


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up method"""
        self.base = BaseModel()
        self.base2 = BaseModel()

    def tearDown(self):
        """Tear down method"""
        del self.base
        del self.base2
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertTrue(len(models.base_model.__doc__) > 0)

    def test_class_docstring(self):
        """Test for the existence of BaseModel class docstring"""
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_methods_docstring(self):
        """Test for the existence of methods docstring"""
        self.assertTrue(len(BaseModel.__init__.__doc__) > 0)
        self.assertTrue(len(BaseModel.__str__.__doc__) > 0)
        self.assertTrue(len(BaseModel.save.__doc__) > 0)
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 0)

    def test_instance(self):
        """Test for correct instantiation of BaseModel"""
        self.assertIsInstance(self.base, BaseModel)

    def test_id_exists(self):
        """Test for existence of id"""
        self.assertTrue(hasattr(self.base, "id"))

    def test_unique_id(self):
        """Test for unique id"""
        self.assertNotEqual(self.base.id, self.base2.id)

    def test_created_at_exists(self):
        """Test for existence of created_at"""
        self.assertTrue(hasattr(self.base, "created_at"))

    def test_type_of_created_at(self):
        """Test for correct type of created_at"""
        self.assertIsInstance(self.base.created_at, datetime)

    def test_updated_at_exists(self):
        """Test for existence of updated_at"""
        self.assertTrue(hasattr(self.base, "updated_at"))

    def test_type_of_updated_at(self):
        """Test for correct type of updated_at"""
        self.assertIsInstance(self.base.updated_at, datetime)

    def test_str_method(self):
        """Test for correct __str__ output"""
        self.base.name = "Holberton"
        self.base.my_number = 89
        string = "[BaseModel] ({}) {}".format(self.base.id, self.base.__dict__)
        self.assertEqual(str(self.base), string)

    def test_save_method(self):
        """Test for correct update of updated_at"""
        first_updated_at = self.base.updated_at
        self.base.save()
        second_updated_at = self.base.updated_at
        self.assertNotEqual(first_updated_at, second_updated_at)

    def test_to_dict_method(self):
        """Test for correct dictionary representation"""
        base_dict = self.base.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)
        self.assertEqual(base_dict['id'], self.base.id)
        self.assertEqual(base_dict['created_at'],
                         self.base.created_at.isoformat())
        self.assertEqual(base_dict['updated_at'],
                         self.base.updated_at.isoformat())
        self.assertEqual(base_dict['__class__'], 'BaseModel')
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')

    def test_kwargs(self):
        """Test for correct instantiation from kwargs"""
        base_dict = self.base.to_dict()
        base_copy = BaseModel(**base_dict)
        self.assertEqual(base_copy.to_dict(), base_dict)
