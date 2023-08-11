#!/usr/bin/python3
"""
AirBnB console command interpreter
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime
from shlex import split
from os import getenv
from pathlib import Path
import re

# Detect if running as script or module
FILE_STORAGE = getenv('HBNB_TYPE_STORAGE')
if FILE_STORAGE == 'db':
    from models import db_storage
    classes = db_storage.DBStorage.CNC.keys()
else:
    classes = storage.all()

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    # ----- Basic Console Commands -----
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    # ----- Custom Console Commands -----
    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        argl = parse(arg)
        if not argl:
            print("** class name missing **")
        elif argl[0] not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = classes[argl[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Usage: show <class> <id>
        Display the string representation of a class instance of a given id.
        """
        argl = parse(arg)
        if len(argl) < 2:
            print("** class name missing **")
        elif argl[0] not in classes:
            print("** class doesn't exist **")
        elif len(argl) < 3:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(argl[0], argl[1])
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Usage: destroy <class> <id>
        Delete a class instance of a given id."""
        argl = parse(arg)
        if len(argl) < 2:
            print("** class name missing **")
        elif argl[0] not in classes:
            print("** class doesn't exist **")
        elif len(argl) < 3:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(argl[0], argl[1])
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Usage: all or all <class>
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        argl = parse(arg)
        if argl and argl[0] not in classes:
            print("** class doesn't exist **")
        else:
            instances = []
            for key, obj in storage.all().items():
                if not argl or argl[0] == obj.__class__.__name__:
                    instances.append(str(obj))
            print(instances)

    def do_count(self, arg):
        """Usage: count <class>
        Retrieve the number of instances of a given class."""
        argl = parse(arg)
        if len(argl) < 1:
            print("** class name missing **")
        elif argl[0] not in classes:
            print("** class doesn't exist **")
        else:
            count = sum(1 for obj in storage.all().values() if obj.__class__.__name__ == argl[0])
            print(count)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        argl = parse(arg)
        if len(argl) < 2:
            print("** class name missing **")
            return
        if argl[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(argl) < 3:
            print("** instance id missing **")
            return
        key = "{}.{}".format(argl[0], argl[1])
        obj_dict = storage.all()
        if key not in obj_dict:
            print("** no instance found **")
            return

        obj = obj_dict[key]
        if len(argl) < 4:
            print("** attribute name missing **")
            return

        attr_name = argl[2]
        if len(argl) < 5:
            print("** value missing **")
            return

        attr_value = argl[3]
        setattr(obj, attr_name
        setattr(obj, attr_name, attr_value)
        obj.save()

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def parse(arg):
         curly_braces = re.search(r"\{(.*?)\}", arg)
         brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl

if __name__ == '__main__':
    HBNBCommand().cmdloop()
    
