#!/usr/bin/python3

"""Unittest for place"""

import unittest
from datetime import datetime
from models.place import Place
import models.place
import os


class TestReview(unittest.TestCase):
    """Test cases for the Place class"""

    def setUp(self):
        """Set up method"""
        self.place = Place()
        self.place2 = Place()

    def tearDown(self):
        """Tear down method"""
        del self.place
        del self.place2
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertTrue(len(models.place.__doc__) > 0)

    def test_class_docstring(self):
        """Test for the existence of BaseModel class docstring"""
        self.assertTrue(len(Place.__doc__) > 0)

    def test_methods_docstring(self):
        """Test for the existence of methods docstring"""
        self.assertTrue(len(Place.__init__.__doc__) > 0)
        self.assertTrue(len(Place.__str__.__doc__) > 0)
        self.assertTrue(len(Place.save.__doc__) > 0)
        self.assertTrue(len(Place.to_dict.__doc__) > 0)

    def test_instance(self):
        """Test for correct instantiation of BaseModel"""
        self.assertIsInstance(self.place, Place)

    def test_id_exists(self):
        """Test for existence of id"""
        self.assertTrue(hasattr(self.place, "id"))

    def test_unique_id(self):
        """Test for unique id"""
        self.assertNotEqual(self.place.id, self.place2.id)

    def test_created_at_exists(self):
        """Test for existence of created_at"""
        self.assertTrue(hasattr(self.place, "created_at"))

    def test_type_of_created_at(self):
        """Test for correct type of created_at"""
        self.assertIsInstance(self.place.created_at, datetime)

    def test_updated_at_exists(self):
        """Test for existence of updated_at"""
        self.assertTrue(hasattr(self.place, "updated_at"))

    def test_type_of_updated_at(self):
        """Test for correct type of updated_at"""
        self.assertIsInstance(self.place.updated_at, datetime)

    def test_str_method(self):
        """Test for correct __str__ output"""
        self.place.name = "Holberton"
        self.place.my_number = 89
        string = "[Place] ({}) {}".format(self.place.id, self.place.__dict__)
        self.assertEqual(str(self.place), string)

    def test_save_method(self):
        """Test for correct update of updated_at"""
        first_updated_at = self.place.updated_at
        self.place.save()
        second_updated_at = self.place.updated_at
        self.assertNotEqual(first_updated_at, second_updated_at)

    def test_to_dict_method(self):
        """Test for correct dictionary representation"""
        base_dict = self.place.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)
        self.assertEqual(base_dict['id'], self.place.id)
        self.assertEqual(base_dict['created_at'], self.place.created_at.isoformat())
        self.assertEqual(base_dict['updated_at'], self.place.updated_at.isoformat())
        self.assertEqual(base_dict['__class__'], 'Place')
        self.assertEqual(self.place.__class__.__name__, 'Place')

    def test_place_city_id(self):
        """Test for correct instantiation of city_id"""
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertEqual(self.place.city_id, "")

    def test_place_user_id(self):
        """Test for correct instantiation of user_id"""
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertEqual(self.place.user_id, "")

    def test_place_name(self):
        """Test for correct instantiation of name"""
        self.assertTrue(hasattr(self.place, "name"))
        self.assertEqual(self.place.name, "")

    def test_place_description(self):
        """Test for correct instantiation of description"""
        self.assertTrue(hasattr(self.place, "description"))
        self.assertEqual(self.place.description, "")

    def test_number_rooms(self):
        """Test for correct instantiation of number_rooms"""
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertEqual(self.place.number_rooms, 0)

    def test_number_bathrooms(self):
        """Test for correct instantiation of number_bathrooms"""
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_max_guest(self):
        """Test for correct instantiation of max_guest"""
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertEqual(self.place.max_guest, 0)

    def test_price_by_night(self):
        """Test for correct instantiation of price_by_night"""
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertEqual(self.place.price_by_night, 0)

    def test_latitude(self):
        """Test for correct instantiation of latitude"""
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertEqual(self.place.latitude, 0.0)

    def test_amenity_ids(self):
        """Test for correct instantiation of amenity_ids"""
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertEqual(self.place.amenity_ids, [])
