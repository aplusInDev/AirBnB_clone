#!/usr/bin/python3
"""
AirBnB console command interpreter.

"""

import cmd
import inspect
import re
import sys

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Command processor for object management.

    """

    prompt = "(hbnb) "

    def convert_to_int(value):
        """Convert value to int if possible."""
        try:
            num = int(value)
            return num
        except:
            return value

    def is_valid_class(class_name):
        """Check if class exists."""
        try:
            result = inspect.isclass(eval(class_name))
            return result
        except:
            return False

    def do_quit(self, line):
        """Quit the command line."""
        return True

    def do_EOF(self, line):
        """Exit on end-of-file marker."""
        print("")
        return True

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def do_create(self, line):
        """
        Usage: create <class>
        Create a new class instance and print its id.
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif HBNBCommand.is_valid_class(args[0]):
            if not issubclass(eval(args[0]), BaseModel):
                print("** class doesn't exist **")
            else:
                new_instance = eval(args[0])()
                new_instance.save()
                print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Usage: show <class> <id>
        Display the string representation of a class instance of a given id.
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif HBNBCommand.is_valid_class(args[0]):
            if not issubclass(eval(args[0]), BaseModel):
                print("** class doesn't exist **")
            else:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    objects = storage.all()
                    if key in objects:
                        print(objects[key])
                    else:
                        print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """
        Usage: destroy <class> <id>
        Delete a class instance of a given id.
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif HBNBCommand.is_valid_class(args[0]):
            if not issubclass(eval(args[0]), BaseModel):
                print("** class doesn't exist **")
            else:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    objects = storage.all()
                    if key in objects:
                        del objects[key]
                        storage.save()
                    else:
                        print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        """
        Usage: all or all <class>
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects.
        """
        args = line.split()
        objs = []
        if len(args) == 0:
            for k, v in storage.all().items():
                objs.append(str(v))
            print(objs)
        elif HBNBCommand.is_valid_class(args[0]):
            if not issubclass(eval(args[0]), BaseModel):
                print("** class doesn't exist **")
            else:
                for k, v in storage.all().items():
                    obj_keys = k.split(".")
                    if obj_keys[0] == args[0]:
                        objs.append(str(v))
                print(objs)
        else:
            print("** class doesn't exist **")


def do_count(self, arg):
    """
    Usage: count <class>
    Retrieve the number of instances of a given class.
    """
    args = arg.split()
    if len(args) == 0:
        print("** class name missing **")
    elif self.is_valid_class(args[0]):
        if not issubclass(eval(args[0]), BaseModel):
            print("** class doesn't exist **")
        else:
            count = sum(
                1 for obj in storage.all().values() if obj.__class__.__name__ == args[0]
            )
            print(count)
    else:
        print("** class doesn't exist **")

    def do_update(self, line):
        """
         Usage: update <class> <id> <attribute_name> <attribute_value> or
        <class>.update(<id>, <attribute_name>, <attribute_value>) or
        <class>.update(<id>, <dictionary>)
         Update a class instance of a given id by adding or updating
         a given attribute key/value pair or dictionary.
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif HBNBCommand.is_valid_class(args[0]):
            if not issubclass(eval(args[0]), BaseModel):
                print("** class doesn't exist **")
            else:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    objects = storage.all()
                    if key in objects:
                        if len(args) == 2:
                            print("** attribute name missing **")
                        else:
                            line2 = line.split('"')
                            if len(line2) == 1:
                                print("** value missing **")
                            else:
                                setattr(objects[key], str(args[2]), str(line2[1]))
                                storage.save()
                    else:
                        print("** no instance found **")
        else:
            print("** class doesn't exist **")


def default(self, line):
    """
    Called when command prefix is not recognized.
    Handles special commands like <class name>.all(), <class name>.count(),
    <class name>.show(<id>), <class name>.destroy(<id>), and <class name>.update(<id>, <dictionary>).
    """
    args = line.split(".")
    class_name = args[0] if args[0] is not None else ""
    if args[1] is not None:
        if args[1] == "all()":
            HBNBCommand.handle_def_all(line, class_name)
        elif args[1] == "count()":
            HBNBCommand.handle_def_count(line, class_name)
        else:
            cmds = re.split('\(|"|\)', args[1])
            cmds = list(filter(None, cmds))
            if cmds[0] == "show":
                HBNBCommand.handle_def_show(class_name, cmds[1])
            elif cmds[0] == "destroy":
                HBNBCommand.handle_def_destroy(class_name, cmds[1])
            elif cmds[0] == "update":
                cmds = re.split("\(|\"|\)|\{|'|\}|: |:|, ", args[1])
                cmds = list(filter(None, cmds))
                if len(cmds) == 4:
                    HBNBCommand.handle_def_update(class_name, cmds[1], cmds[2], cmds[3])
                else:
                    tab = cmds[2:]
                    d = {}
                    for i in range(0, len(tab), 2):
                        d[tab[i]] = tab[i + 1]
                    HBNBCommand.handle_def_update_with_dict(class_name, cmds[1], d)


if __name__ == "__main__":
    HBNBCommand().cmdloop()

    
