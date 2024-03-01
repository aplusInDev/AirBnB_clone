#!/usr/bin/python3
""" This module contains the entry point of the command interpreter"""
from io import StringIO
from console import HBNBCommand
from unittest.mock import patch
import unittest


class TestConsole(unittest.TestCase):
    """Unittest for the console"""
    def test_help(self):
        """Test help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            with patch('sys.stdin', new=StringIO("help\n")):
                HBNBCommand().cmdloop()
                self.assertTrue(len(f.getvalue()) > 0)

    def test_help2(self):
        """Test help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertTrue(len(f.getvalue()) > 0)

    def test_EOF(self):
        """Test EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            with patch('sys.stdin', new=StringIO("EOF\n")):
                HBNBCommand().cmdloop()
                self.assertEqual(f.getvalue(), "(hbnb) \n")

    def test_EOF2(self):
        """Test EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(f.getvalue(), "\n")

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            with patch('sys.stdin', new=StringIO("quit\n")):
                HBNBCommand().cmdloop()
                self.assertEqual(f.getvalue(), "(hbnb) ")

    def test_quit2(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), "")

    def test_emptyline(self):
        """Test emptyline command"""
        with patch('sys.stdout', new=StringIO()) as f:
            with patch('sys.stdin', new=StringIO("\n")):
                HBNBCommand().cmdloop()
                self.assertEqual(f.getvalue(), "(hbnb) (hbnb) \n")

    def test_emptyline2(self):
        """Test emptyline command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual(f.getvalue(), "")

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            with patch('sys.stdin', new=StringIO("create BaseModel\n")):
                HBNBCommand().cmdloop()
                self.assertTrue(len(f.getvalue()) > 0)

    def test_create2(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertTrue(len(f.getvalue()) > 0)

    def test_nonexistent_class(self):
        """Test nonexistent class"""
        with patch('sys.stdout', new=StringIO()) as f:
            with patch('sys.stdin', new=StringIO("create MyModel\n")):
                HBNBCommand().cmdloop()
                self.assertEqual(f.getvalue(), "(hbnb) ** class doesn't exist **\n(hbnb) \n")

    def test_noexistent_class2(self):
        """Test nonexistent class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

if __name__ == "__main__":
    unittest.main()
