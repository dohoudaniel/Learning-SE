#!/usr/bin/python3

"""
Configuring cmd through Attributes
Testing this with the ALX SE Project
"""

import cmd

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""

    prompt = '(hbnb) '
    intro = "Simple command processor example."

    doc_header = 'Documented Commands'
    misc_header = 'Miscallenous Commands'
    undoc_header = 'Undocumented Commands'
    
    ruler = '-'
    
    def do_prompt(self, line):
        "Change the interactive prompt"
        self.prompt = line + ': '

    def do_EOF(self, line):
        """
        Exiting the console
        """
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()

