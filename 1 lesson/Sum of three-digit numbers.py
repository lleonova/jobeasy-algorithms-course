# Our code generates a random three-digit number and has to sum up all its digits. For example, if a number is 349,
# the code has to print the number 16, because 3 + 4 + 9 = 16.

from random import randint

n = 6
123456

n = randint(100, 999)
print(n)

ones = n % 10
tens = (n // 10) % 10
hundreds = n // 100
print(ones + tens + hundreds)

# TODO: Homework: Rewrite a program with any number of digits.
#  Instead of  3 digits, you should sum digits up from n digits number,
#  Where  User enter n manually. n > 0
