# This should be the basic replica of the 'cp' command
# If ran from the command line without arguments
# It should print out the usage:
# copy [source] [destination]
# When just one argument is provided print out
# No destination provided
# When both arguments provided and the source is a file
# Read all contents from it and write it to the destination

import sys

class Control():

    def __init__(self):
        self.list_argv = []
        self.arg_reader()
        self.controller()

    def arg_reader(self):
        if len(sys.argv) <= 1:
            self.list_argv = []
        else:
            self.list_argv = sys.argv[1:]

    def controller(self):
            if len(self.list_argv) == 0:
                display.print_usage()
            if len(self.list_argv) == 1:
                display.print_one_argument()

class Model():
    pass


class Display():

    def print_usage(self):
        print(" Usage:\n copy [source] [destination] \n When just one argument is provided print out \n No destination provided \n When both arguments provided and the source is a file \n Read all contents from it and write it to the destination")

    def print_one_argument(self):
        print("No destination provided")


model = Model()
display = Display()
control = Control()
