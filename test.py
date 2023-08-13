#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.__init__ import storage

class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '
    class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
            }

    def do_help(self, arg):
        '''help (usage: help argument) This command print giving argument
        information'''
        super().do_help(arg)
        print()

    def do_EOF(self, line):
        '''end of file command to exit the program'''
        return True

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        '''Create commant to make new instance of giving class'''
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
        else:
            my_model = HBNBCommand.class_dict[arg]()
            storage.save()
            print(my_model.id)

    def do_show(self, line):
        '''Command prints the string representation of an instance based
        on the class name and
        Usage: show <class name> <instance id>'''
        if not line:
            print("** class name missing **")
            return
        arg_list = line.split(" ")
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        if arg_list[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
            return
        key = arg_list[0] + "." + arg_list[1]
        try:
            # print(storage._FileStorage__objects[key])
             print(storage.all()[key])
        except Exception:
            print("** no instance found **")

    def do_destroy(self, line):
        '''Command destroy a giving instance
        Usage:
            destroy <class name> <instance id>'''
        if not line:
            print("** class name missing **")
            return
        arg_list = line.split(" ")
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        if arg_list[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
            return
        key = arg_list[0] + "." + arg_list[1]
        try:
            del(storage.all()[key])
            storage.save()
        except Exception:
            print("** no instance found **")

    def do_all(self, line):
        '''all command that show all giving class instances
        Usage: all <class name>'''
        if not line or line not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
            return
        all_list = []
        for key, value in storage.all().items():
            if line == key.split(".")[0]:
                all_list.append(str(value))
        print(all_list)

    def do_update(self, line):
        '''update command to update giving instance base on giving
        class name and id by adding or updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"'''
        if not line:
            print("** class name missing **")
            return
        line_list = line.split(" ")
        try:
            class_name = line_list[0]
            instance_id = line_list[1]
            new_attr = line_list[2]
            new_value = line_list[3]
            try:
                new_value = eval(new_value)
            except Exception:
                pass
        except Exception:
            pass
        if line_list[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
            return
        if len(line_list) < 2:
            print("** instance id missing **")
            return
        giving_key = class_name + "." + instance_id
        if giving_key not in storage.all():
            print("** no instance found **")
            return
        if len(line_list) < 3:
            print("** attribute name missing **")
            return
        if len(line_list) < 4:
            print("** value missing **")
            return
        if new_attr in ['updated_at', 'created_at']:
            return
        try:
            new_dict = storage.all()[giving_key]
            new_dict.__dict__.update({new_attr: new_value})
            new_dict.save()
        except Exception:
            pass

    def count(self, arg):
        counter = 0
        for key in storage.all().keys():
            if key.split(".")[0] == arg:
                counter += 1
        print(counter)

    def default(self, line):
        line_list = line.split(".")
        if len(line_list) == 2:
            class_name = line_list[0]
            class_method = line_list[1]
            if class_name in HBNBCommand.class_dict:
                if class_method == 'all()':
                    return self.do_all(class_name)
                if class_method == 'count()':
                    return self.count(class_name)
                if ('.' in line and '(' in line and ')' in line):
                    class_id = line[line.find('(') + 1: line.find(')')]
                    if class_id:
                        class_id = class_id.replace('\"', '')
                        return self.do_show(class_name + " " + class_id)
        return super().default(line)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
