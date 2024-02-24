import math

sides = int(input("sides: "))
length = float(input("length: "))

area = 0.25*sides*length**2/math.tan(math.pi/sides)
print(area)