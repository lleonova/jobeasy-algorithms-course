# 1. The code generates a random n-digits number and has to sum up all its digits.
#    Where User enter n manually. n > 0

# First try, using strings

n = int(input('input a number bigger than 0: '))

if n <= 0:
    print('The number should be bigger than 0 ')
    quit()


from random import randint
number = randint(10 ** (n - 1), (10 ** n) - 1 )

sum = 0
for digit in str(number):
    sum += int(digit)


print(f'{n}-digits number is {number}')
print(f'The sum of its numbers is {sum}')

# Second try, using math

number_leght = int(input('input a number bigger than 0: '))

if number_leght <= 0:
    print('The number should be bigger than 0 ')
    quit()

from random import randint
random_number = randint(10 ** (number_leght - 1), (10 ** number_leght) - 1 )

sum_of_numbers = 0
x = 1
while x <= number_leght:
    sum_of_numbers += (random_number // 10 ** (x-1)) % 10
    x += 1

print(f'{number_leght}-digits number is {random_number}')
print(f'The sum of its numbers is {sum_of_numbers}')


# # 2. Find max number from 3 values, entered manually from a keyboard

print('Please enter three numbers: ')
one = int(input('number one: '))
two = int(input('number two: '))
three = int(input('number three: '))

if one > two and one > three:
    max = one
elif two > one and two > three:
    max = two
else:
    max = three

print(f'The largest number is {max}')

# # 3. Count odd and even numbers.
# # Count odd and even digits of the whole number.
# # E.g, if entered number 34560, then 3 digits will be even (4, 6, and 0)  and  2 odd digits (3 and 5)

number1 = list(input('Please enter any number: '))

even = 0
odd = 0

for digit in number1:
    if int(digit) % 2 == 0:
        even += 1
    else:
        odd += 1

print(f'This number has {even} even and {odd} odd digits')

# Kata 1

# Multiply
# def multiply(a, b):
#   a * b

def multiply(a, b):
  return a * b

# Kata 2

# Create a function called shortcut to remove all the lowercase vowels in a given string.
# Don't worry about uppercase vowels.

def shortcut(s):

    vowels = ['a', 'e', 'i', 'o', 'u' ]

    result = ''
    for letter in s:
        if letter not in vowels:
            result += letter
    return(result)

# Kata 3

# Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.
# Your task is to make 'Past' function which returns time converted to milliseconds.

def past(h, m, s):
     return( (h * 60 * 60 + m * 60 + s ) * 1000)

# Kata 4

# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
# It should look like this:
# Sam Harris => S.H
# Patrick Feeney => P.F

def abbrevName(name):
    return(f'{name[0].upper()}.{name[name.index(" ") + 1].upper()}')