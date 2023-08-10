#!/usr/bin/python3
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

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
        """Create a new instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in models.classes:
            print("** class doesn't exist **")
            return
        new_instance = models.classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key in models.storage.all():
            print(models.storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key in models.storage.all():
            del models.storage.all()[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all instances"""
        if arg and arg not in models.classes:
            print("** class doesn't exist **")
            return
        instances = models.storage.all()
        print([str(instances[key]) for key in instances])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key in models.storage.all():
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            instance = models.storage.all()[key]
            attr_name = args[2]
            attr_value = args[3].strip("\"")
            setattr(instance, attr_name, attr_value)
            instance.save()
        else:
            print("** no instance found **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()

