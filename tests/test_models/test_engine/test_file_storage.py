#!/usr/bin/python3
"""Unittest for FileStorage class"""

import unittest
from models import BaseModel, storage
import os
import json


class TestFileStorage(unittest.TestCase):
    """Test for FileStorage class"""

    def setUp(self):
        """Setup for the test"""
        to_delete = []
        for key in storage.all().keys():
            to_delete.append(key)
        for key in to_delete:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """Tear down for the test"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_empty_objects(self):
        """Test for __objects"""
        self.assertEqual(storage.all(), {})

    def test_all(self):
        """Test for all method"""
        objects_len = len(storage.all())
        b1 = BaseModel()
        self.assertIsInstance(storage.all(), dict)
        self.assertEqual(storage.all(), storage._FileStorage__objects)
        self.assertEqual(len(storage.all()), objects_len + 1)

    def test_new(self):
        """Test for new method"""
        objects_len = len(storage.all())
        b1 = BaseModel()
        storage.new(b1)
        self.assertIn("BaseModel." + b1.id, storage.all().keys())
        self.assertEqual(len(storage.all()), objects_len + 1)

    def test_save(self):
        """Test for save method"""
        b1 = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))
        with open("file.json", "r") as f:
            self.assertIn("BaseModel." + b1.id, f.read())

    def test_reload(self):
        """Test for reload method"""
        b1 = BaseModel()
        to_delete = []
        for key in storage.all().keys():
            to_delete.append(key)
        for key in to_delete:
            del storage._FileStorage__objects[key]
        with open(storage._FileStorage__file_path, "w") as f:
            json.dump({b1.__class__.__name__ + "." + b1.id: b1.to_dict()}, f)
        objects_len = len(storage.all())
        storage.reload()
        self.assertEqual(len(storage.all()), objects_len + 1)
        self.assertIn("BaseModel." + b1.id, storage.all().keys())
