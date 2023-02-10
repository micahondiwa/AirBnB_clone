#!/usr/bin/python3
"""The console"""

import cmd
class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def do_quit(self, *args):
        return True

    def do_EOF(self, *args):
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
