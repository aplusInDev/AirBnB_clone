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

    def do_BaseModel_all(self, arg):
        """Prints all string representation of all instances"""
        self.do_all(arg)

    def do_User_all(self, arg):
        """Prints all string representation of all User instances"""
        self.do_all(arg)

    def do_Place_all(self, arg):
        """Prints all string representation of all Place instances"""
        self.do_all(arg)

    def do_State_all(self, arg):
        """Prints all string representation of all State instances"""
        self.do_all(arg)

    def do_City_all(self, arg):
        """Prints all string representation of all City instances"""
        self.do_all(arg)

    def do_Amenity_all(self, arg):
        """Prints all string representation of all Amenity instances"""
        self.do_all(arg)

    def do_Review_all(self, arg):
        """Prints all string representation of all Review instances"""
        self.do_all(arg)

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if not arg:
            print([str(obj) for obj in storage.all().values()])
        else:
            args = arg.split()
            if args[0] not in HBNBCommand.valid_classes:
                print("** class doesn't exist **")
                return
            print(
                [
                    str(obj)
                    for obj in storage.all().values()
                    if obj.__class__.__name__ == args[0]
                ]
            )

    def do_State_count(self, arg):
        """Retrieves the number of State instances"""
        self.do_count(arg)

    def do_City_count(self, arg):
        """Retrieves the number of City instances"""
        self.do_count(arg)

    def do_Place_count(self, arg):
        """Retrieves the number of Place instances"""
        self.do_count(arg)

    def do_Review_count(self, arg):
        """Retrieves the number of Review instances"""
        self.do_count(arg)

    def do_count(self, arg):
        """Retrieves the number of instances of a class"""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]
        if class_name in self.valid_classes:
            instances = storage.count(class_name)
            print(instances)
        else:
            print("** class doesn't exist **")

    def do_State_show(self, arg):
        """Prints the string representation of a State instance"""
        self.do_show("State " + arg)

    def do_City_show(self, arg):
        """Prints the string representation of a City instance"""
        self.do_show("City " + arg)

    def do_Amenity_show(self, arg):
        """Prints the string representation of an Amenity instance"""
        self.do_show("Amenity " + arg)

    def do_Place_show(self, arg):
        """Prints the string representation of a Place instance"""
        self.do_show("Place " + arg)

    def do_Review_show(self, arg):
        """Prints the string representation of a Review instance"""
        self.do_show("Review " + arg)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name in self.classes:
            if len(args) < 2:
                print("** instance id missing **")
                return

            instance_id = args[1]
            key = f"{class_name}.{instance_id}"
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_State_destroy(self, arg):
        """Deletes a State instance"""
        self.do_destroy("State " + arg)

    def do_City_destroy(self, arg):
        """Deletes a City instance"""
        self.do_destroy("City " + arg)

    def do_Amenity_destroy(self, arg):
        """Deletes an Amenity instance"""
        self.do_destroy("Amenity " + arg)

    def do_Place_destroy(self, arg):
        """Deletes a Place instance"""
        self.do_destroy("Place " + arg)

    def do_Review_destroy(self, arg):
        """Deletes a Review instance"""
        self.do_destroy("Review " + arg)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name in self.classes:
            if len(args) < 2:
                print("** instance id missing **")
                return

            instance_id = args[1]
            key = f"{class_name}.{instance_id}"
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")


    def do_State_update(self, arg):
        """Updates an instance based on the class name and id"""
        self.do_update("State " + arg)


    def do_City_update(self, arg):
        """Updates an instance based on the class name and id"""
        self.do_update("City " + arg)


    def do_Amenity_update(self, arg):
        """Updates an instance based on the class name and id"""
        self.do_update("Amenity " + arg)


    def do_Place_update(self, arg):
        """Updates an instance based on the class name and id"""
        self.do_update("Place " + arg)


    def do_Review_update(self, arg):
        """Updates an instance based on the class name and id"""
        self.do_update("Review " + arg)


    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name in self.classes:
            if len(args) < 2:
                print("** instance id missing **")
                return

            instance_id = args[1]
            key = f"{class_name}.{instance_id}"
            if key in storage.all():
                instance = storage.all()[key]
                if len(args) < 3:
                    print("** attribute name missing **")
                    return

                attr_name = args[2]
                if len(args) < 4:
                    print("** value missing **")
                    return

                attr_value = args[3]
                setattr(instance, attr_name, attr_value)
                instance.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()

