#!/usr/bin/python3

"""
Shelling out..
Run this in WSL
"""

import cmd
import os

class ShellEnabled(cmd.Cmd):

    prompt = "(hbnb) "    
    last_output = ''    # a class variable used to store the output of the last shell command executed through the do_shell method.

    def do_shell(self, line):
        "Run a shell command"
        print ("Running shell command: ", line)
        output = os.popen(line).read()   # Execute the shell command and capture its output.
        print (output)
        self.last_output = output
    
    def do_echo(self, line):
        "Print the input, replacing '$out' with the output of the last shell command"
        # Obviously not robust
        print (line.replace('$out', self.last_output))
    
    def do_EOF(self, line):
        """
        Exiting shell
        """
        print("Exiting shell...")
        return True
    
if __name__ == '__main__':
    ShellEnabled().cmdloop()
