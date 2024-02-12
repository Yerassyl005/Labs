"""Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for 
   the conversion: C = (5 / 9) * (F – 32)
"""

def fahrenheit_to_centigrade():
    fahrenheit = float(input())
    centigrade = (5 / 9) * (fahrenheit - 32)
    print(centigrade)

fahrenheit_to_centigrade()