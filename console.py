#!/usr/bin/python3
"""The console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """The HBNB class with command line"""

    prompt = 'hbnb '

    def do_create(self, line):
        if not line:
            print("** class name missing **")
        else:
            # Implement code to create a new instance
            pass

    def do_show(self, line):
        if not line:
            print("** class name missing **")
        else:
            # code to show string
            pass

    def do_destroy(self, line):
        if not line:
            print("** class name missing **")
        else:
            # code to delete instance
            pass

    def do_all(self, line):
        # code to print all strings
        pass

    def do_update(self, line):
        if not line:
            print("** Class name missing **")
        else:
            # updating
            pass

    def do_quit(self, *args):
        return True

    def do_EOF(self, *args):
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
