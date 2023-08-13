#!/usr/bin/python3
"""
Unit tests for models/base_model.py
Test classes:
    TestBaseModelInstantiation
    TestBaseModelSave
    TestBaseModelToDict
"""
import os
import unittest
from datetime import datetime
from time import sleep

import models
from models.base_model import BaseModel


class TestBaseModelInstantiation(unittest.TestCase):
    """Test cases for BaseModel class instantiation."""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_two_models_different_created_at(self):
        model1 = BaseModel()
        sleep(0.05)
        model2 = BaseModel()
        self.assertLess(model1.created_at, model2.created_at)

    def test_two_models_different_updated_at(self):
        model1 = BaseModel()
        sleep(0.05)
        model2 = BaseModel()
        self.assertLess(model1.updated_at, model2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        model = BaseModel()
        model.id = "123456"
        model.created_at = model.updated_at = dt
        model_str = model.__str__()
        self.assertIn("[BaseModel] (123456)", model_str)
        self.assertIn("'id': '123456'", model_str)
        self.assertIn("'created_at': " + dt_repr, model_str)
        self.assertIn("'updated_at': " + dt_repr, model_str)

    def test_args_unused(self):
        model = BaseModel(None)
        self.assertNotIn(None, model.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        model = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(model.id, "345")
        self.assertEqual(model.created_at, dt)
        self.assertEqual(model.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        model = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(model.id, "345")
        self.assertEqual(model.created_at, dt)
        self.assertEqual(model.updated_at, dt)


class TestBaseModelSave(unittest.TestCase):
    """Test cases for BaseModel class save method."""

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
        model = BaseModel()
        sleep(0.05)
        first_updated_at = model.updated_at
        model.save()
        self.assertLess(first_updated_at, model.updated_at)

    def test_two_saves(self):
        model = BaseModel()
        sleep(0.05)
        first_updated_at = model.updated_at
        model.save()
        second_updated_at = model.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        model.save()
        self.assertLess(second_updated_at, model.updated_at)

    def test_save_with_arg(self):
        model = BaseModel()
        with self.assertRaises(TypeError):
            model.save(None)

    def test_save_updates_file(self):
        model = BaseModel()
        model.save()
        modelid = "BaseModel." + model.id
        with open("file.json", "r") as f:
            self.assertIn(modelid, f.read())


class TestBaseModelToDict(unittest.TestCase):
    """Test cases for BaseModel class to_dict method."""

    def test_to_dict_type(self):
        model = BaseModel()
        self.assertTrue(dict, type(model.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        model = BaseModel()
        self.assertIn("id", model.to_dict())
        self.assertIn("created_at", model.to_dict())
        self.assertIn("updated_at", model.to_dict())
        self.assertIn("__class__", model.to_dict())

    def test_to_dict_contains_added_attributes(self):
        model = BaseModel()
        model.name = "Holberton"
        model.my_number = 98
        self.assertIn("name", model.to_dict())
        self.assertIn("my_number", model.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(str, type(model_dict["created_at"]))
        self.assertEqual(str, type(model_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        model = BaseModel()
        model.id = "123456"
        model.created_at = model.updated_at = dt
        tdict = {
            "id": "123456",
            "__class__": "BaseModel",
            "created_at": dt.isoformat(),
            "updated_at": dt.isoformat(),
        }
        self.assertDictEqual(model.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        model = BaseModel()
        self.assertNotEqual(model.to_dict(), model.__dict__)

    def test_to_dict_with_arg(self):
        model = BaseModel()
        with self.assertRaises(TypeError):
            model.to_dict(None)


if __name__ == "__main__":
    unittest.main()
