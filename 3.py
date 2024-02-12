"""Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many 
   rabbits and how many chickens do we have? create function: solve(numheads, numlegs):
"""

def solution(numheads, numlegs):
    rabbits = 0
    chickens = 0

    if(numlegs % 2 != 0 or numheads >= numlegs):
        print("No solution")
    else:
        rabbits = (numlegs - 2*numheads)/2
        chickens = numheads - rabbits
        print(f"A total number of rabbits: {int(rabbits)} \nA total number of chickens: {int(chickens)}")

solution(35, 94)