#!/usr/bin/python3
import cmd
import sys

import models
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]

    def emptyline(self):
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the console with Ctrl-D"""
        return True

    def help_EOF(self):
        """Documented help message for EOF"""
        print("Exit the console with Ctrl-D")

    def help_quit(self):
        """Documented help message for quit"""
        print("Quit command to exit the program")

    def do_create(self, arg):
        """Create a new instance of BaseModel or a subclass"""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]
        if class_name not in valid_classes:
            print("** class doesn't exist **")
            return

        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{class_name}.{args[1]}"
        all_objs = storage.all()
        if key in all_objs:
            obj = all_objs[key]
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{class_name}.{args[1]}"
        all_objs = storage.all()
        if key in all_objs:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{class_name}.{args[1]}"
        all_objs = storage.all()
        if key in all_objs:
            obj = all_objs[key]
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            setattr(obj, args[2], args[3])
            obj.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all instances"""
        args = arg.split()
        if not args or args[0] in valid_classes:
            all_objs = storage.all()
            objs_list = []
            if args:
                class_name = args[0]
                for key, obj in all_objs.items():
                    if class_name in key:
                        objs_list.append(str(obj))
            else:
                objs_list = [str(obj) for obj in all_objs.values()]
            print(objs_list)
        else:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()

