#!/usr/bin/python3

#import modules are used here -- sys is a very standard one
import sys

# Gather our code in the main function
def main():
    print("Welcome, Daniel", sys.argv[1])
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
        main()
