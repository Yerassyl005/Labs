# Write a function that takes in a list of integers and returns True if it contains 007 in order

def o_o_seven(ints):
    for i in range(len(ints) - 1):
        if ints[i:i+2] == [0, 0] and ints[i+1:i+3] == [0, 7]:
            return True
    return False

print(o_o_seven([2, 3, 0, 0, 8, 4, 3]))
    