#!/usr/bin/python3
import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()

