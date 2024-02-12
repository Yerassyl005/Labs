"""You are given list of numbers separated by spaces. Write a function filter_prime which will take list of numbers as an agrument 
   and returns only prime numbers from the list.
"""

def filter_prime(list):
    primes = []
    for i in list:
        c = 0
        for j in range(1, i):
            if i%j == 0:
                c+=1
        if c == 1:
            primes.append(i)

    print(primes)
        
    
filter_prime([11, 12, 13, 17])
    