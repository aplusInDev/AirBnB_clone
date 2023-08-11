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
        """Create a new instance of a class."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[class_name]()
        for pair in args[1:]:
            attribute = pair.split("=")
            attr_name = attribute[0]
            attr_value = attribute[1]
            try:
                attr_value = eval(attr_value)
            except (NameError, SyntaxError):
                pass
            setattr(new_instance, attr_name, attr_value)
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Display the string representation of an instance."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in HBNBCommand.instances:
            print(HBNBCommand.instances[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in HBNBCommand.instances:
            del HBNBCommand.instances[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all instances or instances of a specific class."""
        if not arg:
            all_instances = list(HBNBCommand.instances.values())
        else:
            args = arg.split()
            class_name = args[0]
            if class_name not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            all_instances = [
                instance
                for key, instance in HBNBCommand.instances.items()
                if key.split(".")[0] == class_name
            ]
        print(all_instances)

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in HBNBCommand.instances:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3]
        instance = HBNBCommand.instances[key]
        setattr(instance, attr_name, attr_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

