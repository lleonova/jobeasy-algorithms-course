# When User enters a number, its factorial is displayed.
import math

n = int(input('Input a number '))


def factorial(number):
    # result = 1
    #
    # if number < 0:
    #     return f'Are you sure you\'d like to calculate gamma-functions?'
    # for item in range(1, number + 1):
    #     result *= item
    # return result
    return math.factorial(number)

print(factorial(n))
