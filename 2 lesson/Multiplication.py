# Write a Python program to multiply two integers without using the * operator in python


def multiplication(number_1, number_2):
    iterator = 0
    result = 0
    while iterator < number_1:
        result += number_2
        iterator += 1
    return result


print(multiplication(6, 6))
print(6 * 6)
