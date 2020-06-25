# When User enters a number, its factorial is displayed.
import math

n = int(input('Input a number '))


def factorial(number):
    if number < 0:
        return f'Are you sure you\'d like to calculate gamma-functions?'
    elif number == 0:
        return(1)
    elif number == 1:
        return(1)
    return(factorial(number-1) * number)

print(factorial(n))
