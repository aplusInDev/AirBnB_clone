#!/usr/bin/python3
"""
Unit tests for models/review.py.
Test classes:
    TestReviewInstantiation
    TestReviewSave
    TestReviewToDict
"""
import os
import unittest
from datetime import datetime
from time import sleep

import models
from models.review import Review


class TestReviewInstantiation(unittest.TestCase):
    """Unit tests for instantiating the Review class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_class_attribute(self):
        review_inst = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(review_inst))
        self.assertNotIn("place_id", review_inst.__dict__)

    def test_user_id_is_public_class_attribute(self):
        review_inst = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(review_inst))
        self.assertNotIn("user_id", review_inst.__dict__)

    def test_text_is_public_class_attribute(self):
        review_inst = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(review_inst))
        self.assertNotIn("text", review_inst.__dict__)

    def test_two_reviews_unique_ids(self):
        review_inst1 = Review()
        review_inst2 = Review()
        self.assertNotEqual(review_inst1.id, review_inst2.id)

    def test_two_reviews_different_created_at(self):
        review_inst1 = Review()
        sleep(0.05)
        review_inst2 = Review()
        self.assertLess(review_inst1.created_at, review_inst2.created_at)

    def test_two_reviews_different_updated_at(self):
        review_inst1 = Review()
        sleep(0.05)
        review_inst2 = Review()
        self.assertLess(review_inst1.updated_at, review_inst2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        review_inst = Review()
        review_inst.id = "123456"
        review_inst.created_at = review_inst.updated_at = dt
        review_inststr = review_inst.__str__()
        self.assertIn("[Review] (123456)", review_inststr)
        self.assertIn("'id': '123456'", review_inststr)
        self.assertIn("'created_at': " + dt_repr, review_inststr)
        self.assertIn("'updated_at': " + dt_repr, review_inststr)

    def test_args_unused(self):
        review_inst = Review(None)
        self.assertNotIn(None, review_inst.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        review_inst = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(review_inst.id, "345")
        self.assertEqual(review_inst.created_at, dt)
        self.assertEqual(review_inst.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class TestReviewSave(unittest.TestCase):
    """Unit tests for the save method of the Review class."""

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
        review_inst = Review()
        sleep(0.05)
        first_updated_at = review_inst.updated_at
        review_inst.save()
        self.assertLess(first_updated_at, review_inst.updated_at)

    def test_two_saves(self):
        review_inst = Review()
        sleep(0.05)
        first_updated_at = review_inst.updated_at
        review_inst.save()
        second_updated_at = review_inst.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        review_inst.save()
        self.assertLess(second_updated_at, review_inst.updated_at)

    def test_save_with_arg(self):
        review_inst = Review()
        with self.assertRaises(TypeError):
            review_inst.save(None)

    def test_save_updates_file(self):
        review_inst = Review()
        review_inst.save()
        review_instid = "Review." + review_inst.id
        with open("file.json", "r") as f:
            self.assertIn(review_instid, f.read())


class TestReviewToDict(unittest.TestCase):
    """Unit tests for the to_dict method of the Review class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        review_inst = Review()
        self.assertIn("id", review_inst.to_dict())
        self.assertIn("created_at", review_inst.to_dict())
        self.assertIn("updated_at", review_inst.to_dict())
        self.assertIn("__class__", review_inst.to_dict())

    def test_to_dict_contains_added_attributes(self):
        review_inst = Review()
        review_inst.middle_name = "Holberton"
        review_inst.my_number = 98
        self.assertEqual("Holberton", review_inst.middle_name)
        self.assertIn("my_number", review_inst.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        review_inst = Review()
        review_inst_dict = review_inst.to_dict()
        self.assertEqual(str, type(review_inst_dict["id"]))
        self.assertEqual(str, type(review_inst_dict["created_at"]))
        self.assertEqual(str, type(review_inst_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        review_inst = Review()
        review_inst.id = "123456"
        review_inst.created_at = review_inst.updated_at = dt
        tdict = {
            "id": "123456",
            "__class__": "Review",
            "created_at": dt.isoformat(),
            "updated_at": dt.isoformat(),
        }
        self.assertDictEqual(review_inst.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        review_inst = Review()
        self.assertNotEqual(review_inst.to_dict(), review_inst.__dict__)

    def test_to_dict_with_arg(self):
        review_inst = Review()
        with self.assertRaises(TypeError):
            review_inst.to_dict(None)


if __name__ == "__main__":
    unittest.main()

