# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def three_three(ints):
    for i in range(len(ints) - 1):
        if ints[i:i+2] == [3, 3]:
            return True
    return False

print(three_three([2, 3, 0, 4, 3]))
    