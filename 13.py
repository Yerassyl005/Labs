"""
Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. 
This is how it should work when run in a terminal:

Hello! What is your name? 
KBTU

Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12

Your guess is too low.
Take a guess.
16

Your guess is too low.
Take a guess.
19

Good job, KBTU! You guessed my number in 3 guesses!
"""

def guess_the_num(num):
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    max_tries = 5
    counter = 0

    for i in range(max_tries):
        guess = int(input("Take a guess.\n"))

        if(guess > 20 or guess < 1):
            print("A number should be between 1 and 20. \n")

        elif(guess < num):
            print("Your guess is too low.")
        elif(guess > num):
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {counter} guesses!")
            break
    else:
        print(f"Sorry, {name}. You are out of tries. The number was {num}.")
        
num = int(input())
if(num < 1):
    print("Guessing number should be between 1 and 20.")
elif(num > 20):
    print("Guessing number should be between 1 and 20.")

guess_the_num(num)
