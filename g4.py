import math

def generator(a,b):
    for number in range(a,b+1):
        yield number**2

a = int(input("a: "))
b = int(input("b: "))

squares = generator(a,b)

for i in squares:
    print(i)