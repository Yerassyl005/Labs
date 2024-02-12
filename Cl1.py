#Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.

class stringManipulator:
    def __init__(self):
        self.input_str = ""
    def getString(self):
        self.input_str = input()
    def printString(self):
        print(self.input_str.upper())

myStr = stringManipulator()

myStr.getString()
myStr.printString()
