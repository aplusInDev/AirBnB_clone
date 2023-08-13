#!/usr/bin/python3
"""This module test console module"""

import unittest
import console
from console import HBNBCommand


class test_console(unittest.TestCase):
    """Tests console module"""

    def create(self):
        """create new intance"""
        return HBNBCommand()

    def test_quit(self):
        """Tests quit command"""
        con = self.create()
        self.assertTrue(con.onecmd("quit"))

    def test_EOF(self):
        """Tests EOF command"""
        con = self.create()
        self.assertTrue(con.onecmd("EOF"))
