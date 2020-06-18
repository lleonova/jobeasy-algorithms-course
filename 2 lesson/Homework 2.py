# 1. Zeros not for Heros
# Numbers ending with zeros are boring.
# They might be fun in your world, but not here.
# Get rid of them. Only the ending ones.
#
# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105
# Zero alone is fine, don't worry about it. Poor guy anyway

def removing_zeros(number):

    if number == 0:
        return(0)

    result = str(number)

    while result[-1] == '0':
        result = result[:-1]

    return(result)

print(removing_zeros(1023000))



# 2. Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n.
# If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
# This is only applicable to the natural numbers.

# 16  -->  1 + 6 = 7
# 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2


def digital_root(number):
    result = number

    while number > 9:
        result = 0
        for item in str(number):
            result += int(item)
            number = result
    return(result)

print(digital_root(1512))




