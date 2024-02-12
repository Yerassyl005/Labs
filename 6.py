# Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We

def reverse_str(str):
    list = str.split(' ')
    print(" ".join(list[::-1]))

str = input()

reverse_str(str)