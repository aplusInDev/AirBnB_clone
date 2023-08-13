#!/usr/bin/python3
"""
Test suite for models/place.py.
Unittest classes:
    TestPlaceInstantiation
    TestPlaceSave
    TestPlaceToDict
"""
import os
import unittest
from datetime import datetime
from time import sleep

import models
from models.place import Place


class TestPlaceInstantiation(unittest.TestCase):
    """Tests instantiation of the Place class."""

    def test_no_args_create(self):
        self.assertEqual(Place, type(Place()))

    def test_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_public_attribute(self):
        Place = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(Place))
        self.assertNotIn("city_id", Place.__dict__)

    def test_user_id_public_attribute(self):
        Place = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(Place))
        self.assertNotIn("user_id", Place.__dict__)

    def test_name_public_attribute(self):
        Place = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(Place))
        self.assertNotIn("name", Place.__dict__)

    def test_description_public_attribute(self):
        Place = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(Place))
        self.assertNotIn("desctiption", Place.__dict__)

    def test_number_rooms_public_attribute(self):
        Place = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(Place))
        self.assertNotIn("number_rooms", Place.__dict__)

    def test_number_bathrooms_public_attribute(self):
        Place = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(Place))
        self.assertNotIn("number_bathrooms", Place.__dict__)

    def test_max_guest_public_attribute(self):
        Place = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(Place))
        self.assertNotIn("max_guest", Place.__dict__)

    def test_price_by_night_public_attribute(self):
        Place = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(Place))
        self.assertNotIn("price_by_night", Place.__dict__)

    def test_latitude_public_attribute(self):
        Place = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(Place))
        self.assertNotIn("latitude", Place.__dict__)

    def test_longitude_public_attribute(self):
        Place = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(Place))
        self.assertNotIn("longitude", Place.__dict__)

    def test_amenity_ids_public_attribute(self):
        Place = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(Place))
        self.assertNotIn("amenity_ids", Place.__dict__)

    def test_two_places_unique_ids(self):
        Place1 = Place()
        Place2 = Place()
        self.assertNotEqual(Place1.id, Place2 .id)

    def test_two_places_different_created_at(self):
        Place1 = Place()
        sleep(0.05)
        Place2 = Place()
        self.assertLess(Place1.created_at, Place2 .created_at)

    def test_two_places_different_updated_at(self):
        Place1 = Place()
        sleep(0.05)
        Place2 = Place()
        self.assertLess(Place1.updated_at, Place2 .updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        Place = Place()
        Place.id = "123456"
        Place.created_at = Place.updated_at = dt
        plstr = Place.__str__()
        self.assertIn("[Place] (123456)", plstr)
        self.assertIn("'id': '123456'", plstr)
        self.assertIn("'created_at': " + dt_repr, plstr)
        self.assertIn("'updated_at': " + dt_repr, plstr)

    def test_args_unused(self):
        Place = Place(None)
        self.assertNotIn(None, Place.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        Place = Place(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(Place.id, "345")
        self.assertEqual(Place.created_at, dt)
        self.assertEqual(Place.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlaceSave(unittest.TestCase):
    """Tests the save method of the Place class."""

    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        Place = Place()
        sleep(0.05)
        first_updated_at = Place.updated_at
        Place.save()
        self.assertLess(first_updated_at, Place.updated_at)

    def test_two_saves(self):
        Place = Place()
        sleep(0.05)
        first_updated_at = Place.updated_at
        Place.save()
        second_updated_at = Place.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        Place.save()
        self.assertLess(second_updated_at, Place.updated_at)

    def test_save_with_arg(self):
        Place = Place()
        with self.assertRaises(TypeError):
            Place.save(None)

    def test_save_updates_file(self):
        Place = Place()
        Place.save()
        plid = "Place." + Place.id
        with open("file.json", "r") as f:
            self.assertIn(plid, f.read())


class TestPlaceToDict(unittest.TestCase):
    """Tests the to_dict method of the Place class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        Place = Place()
        self.assertIn("id", Place.to_dict())
        self.assertIn("created_at", Place.to_dict())
        self.assertIn("updated_at", Place.to_dict())
        self.assertIn("__class__", Place.to_dict())

    def test_to_dict_contains_added_attributes(self):
        Place = Place()
        Place.middle_name = "Holberton"
        Place.my_number = 98
        self.assertEqual("Holberton", Place.middle_name)
        self.assertIn("my_number", Place.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        Place = Place()
        pl_dict = Place.to_dict()
        self.assertEqual(str, type(pl_dict["id"]))
        self.assertEqual(str, type(pl_dict["created_at"]))
        self.assertEqual(str, type(pl_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        Place = Place()
        Place.id = "123456"
        Place.created_at = Place.updated_at = dt
        tdict = {
            "id": "123456",
            "__class__": "Place",
            "created_at": dt.isoformat(),
            "updated_at": dt.isoformat(),
        }
        self.assertDictEqual(Place.to_dict(), tdict)

    def test_to_dict_differs_from_instance_dict(self):
        Place = Place()
        self.assertNotEqual(Place.to_dict(), Place.__dict__)

    def test_to_dict_with_arg_raises_error(self):
        Place = Place()
        with self.assertRaises(TypeError):
            Place.to_dict(None)


if __name__ == "__main__":
    unittest.main()

