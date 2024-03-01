#!/usr/bin/python3

"""Unittest for review"""

import unittest
from datetime import datetime
from models.review import Review
import models.review
import os


class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    def setUp(self):
        """Set up method"""
        self.review = Review()
        self.review2 = Review()

    def tearDown(self):
        """Tear down method"""
        del self.review
        del self.review2
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertTrue(len(models.review.__doc__) > 0)

    def test_class_docstring(self):
        """Test for the existence of BaseModel class docstring"""
        self.assertTrue(len(Review.__doc__) > 0)

    def test_methods_docstring(self):
        """Test for the existence of methods docstring"""
        self.assertTrue(len(Review.__init__.__doc__) > 0)
        self.assertTrue(len(Review.__str__.__doc__) > 0)
        self.assertTrue(len(Review.save.__doc__) > 0)
        self.assertTrue(len(Review.to_dict.__doc__) > 0)

    def test_instance(self):
        """Test for correct instantiation of BaseModel"""
        self.assertIsInstance(self.review, Review)

    def test_id_exists(self):
        """Test for existence of id"""
        self.assertTrue(hasattr(self.review, "id"))

    def test_unique_id(self):
        """Test for unique id"""
        self.assertNotEqual(self.review.id, self.review2.id)

    def test_created_at_exists(self):
        """Test for existence of created_at"""
        self.assertTrue(hasattr(self.review, "created_at"))

    def test_type_of_created_at(self):
        """Test for correct type of created_at"""
        self.assertIsInstance(self.review.created_at, datetime)

    def test_updated_at_exists(self):
        """Test for existence of updated_at"""
        self.assertTrue(hasattr(self.review, "updated_at"))

    def test_type_of_updated_at(self):
        """Test for correct type of updated_at"""
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_str_method(self):
        """Test for correct __str__ output"""
        self.review.name = "Holberton"
        self.review.my_number = 89
        string = "[Review] ({}) {}".format(self.review.id, self.review.__dict__)
        self.assertEqual(str(self.review), string)

    def test_save_method(self):
        """Test for correct update of updated_at"""
        first_updated_at = self.review.updated_at
        self.review.save()
        second_updated_at = self.review.updated_at
        self.assertNotEqual(first_updated_at, second_updated_at)

    def test_to_dict_method(self):
        """Test for correct dictionary representation"""
        base_dict = self.review.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)
        self.assertEqual(base_dict['id'], self.review.id)
        self.assertEqual(base_dict['created_at'], self.review.created_at.isoformat())
        self.assertEqual(base_dict['updated_at'], self.review.updated_at.isoformat())
        self.assertEqual(base_dict['__class__'], 'Review')
        self.assertEqual(self.review.__class__.__name__, 'Review')

    def test_review_place_id(self):
        """Test for correct instantiation of place_id"""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertEqual(self.review.place_id, "")

    def test_review_user_id(self):
        """Test for correct instantiation of user_id"""
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertEqual(self.review.user_id, "")

    def test_review_text(self):
        """Test for correct instantiation of text"""
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.text, "")
