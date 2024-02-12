"""Define a functino histogram() that takes a list of integers and prints a histogram to the screen. For example, 
   # histogram([4, 9, 7]) should print the following: {**** \n ********* \n *******}
"""

def histogram(list):
    for n in list:
        print(n * '*')

histogram([4, 9, 7])
