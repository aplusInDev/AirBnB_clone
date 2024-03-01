#!/usr/bin/python3

"""Unittest for user"""

import unittest
from datetime import datetime
from models.user import User
import models.user
import os


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def setUp(self):
        """Set up method"""
        self.user = User()
        self.user2 = User()

    def tearDown(self):
        """Tear down method"""
        del self.user
        del self.user2
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertTrue(len(models.user.__doc__) > 0)

    def test_class_docstring(self):
        """Test for the existence of BaseModel class docstring"""
        self.assertTrue(len(User.__doc__) > 0)

    def test_methods_docstring(self):
        """Test for the existence of methods docstring"""
        self.assertTrue(len(User.__init__.__doc__) > 0)
        self.assertTrue(len(User.__str__.__doc__) > 0)
        self.assertTrue(len(User.save.__doc__) > 0)
        self.assertTrue(len(User.to_dict.__doc__) > 0)

    def test_instance(self):
        """Test for correct instantiation of BaseModel"""
        self.assertIsInstance(self.user, User)

    def test_id_exists(self):
        """Test for existence of id"""
        self.assertTrue(hasattr(self.user, "id"))

    def test_unique_id(self):
        """Test for unique id"""
        self.assertNotEqual(self.user.id, self.user2.id)

    def test_created_at_exists(self):
        """Test for existence of created_at"""
        self.assertTrue(hasattr(self.user, "created_at"))

    def test_type_of_created_at(self):
        """Test for correct type of created_at"""
        self.assertIsInstance(self.user.created_at, datetime)

    def test_updated_at_exists(self):
        """Test for existence of updated_at"""
        self.assertTrue(hasattr(self.user, "updated_at"))

    def test_type_of_updated_at(self):
        """Test for correct type of updated_at"""
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_str_method(self):
        """Test for correct __str__ output"""
        self.user.name = "Holberton"
        self.user.my_number = 89
        string = "[User] ({}) {}".format(self.user.id, self.user.__dict__)
        self.assertEqual(str(self.user), string)

    def test_save_method(self):
        """Test for correct update of updated_at"""
        first_updated_at = self.user.updated_at
        self.user.save()
        second_updated_at = self.user.updated_at
        self.assertNotEqual(first_updated_at, second_updated_at)

    def test_to_dict_method(self):
        """Test for correct dictionary representation"""
        base_dict = self.user.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)
        self.assertEqual(base_dict['id'], self.user.id)
        self.assertEqual(base_dict['created_at'],
                         self.user.created_at.isoformat())
        self.assertEqual(base_dict['updated_at'],
                         self.user.updated_at.isoformat())
        self.assertEqual(base_dict['__class__'], 'User')
        self.assertEqual(self.user.__class__.__name__, 'User')

    def test_user_email(self):
        """Test for user email"""
        self.user.email = "my.user@mail.com"
        self.assertEqual(self.user.email, "my.user@mail.com")

    def test_user_password(self):
        """Test for user password"""
        self.user.password = "my_password"
        self.assertEqual(self.user.password, "my_password")

    def test_user_first_name(self):
        """Test for user first name"""
        self.user.first_name = "John"
        self.assertEqual(self.user.first_name, "John")

    def test_user_last_name(self):
        """Test for user last name"""
        self.user.last_name = "Doe"
        self.assertEqual(self.user.last_name, "Doe")
