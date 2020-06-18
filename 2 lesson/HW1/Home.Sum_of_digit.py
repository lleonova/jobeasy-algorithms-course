# TODO: Homework: Rewrite a program with any number of digits.
#  Instead of  3 digits, you should sum digits up from n digits number,
#  Where User enter n manually. n > 0

from random import randint

n = int(input("Enter a number of digits "))

# digits = 5 84621
# (10000, 99999)
# (1000, 9999)
# (100, 999)


def sum_of_digits(digits):
    if digits < 1:
        print('Wrong value. Number should contain at least 1 digit')
        quit()
    down = 10 ** (digits - 1)
    up = 10 ** digits - 1
    n = randint(down, up)
    print(f'We got the number {n}')

    result = 0
    i = 0
    while i < digits:
        result += n % 10
        n = n // 10
        i += 1
    print(f'The result is {result}')


sum_of_digits(n)
