# Find max number from 3 values, entered manually from a keyboard.


num1 = int(input(f"First number "))
num2 = int(input(f"Second number "))
num3 = int(input(f"Third number "))


def max_of_three(number_1, number_2, number_3):
    if number_1 > number_2:
        if number_1 > number_3:
            print(f"The greatest number in range is {number_1}")
        else:
            print(f"The greatest number in range is {number_3}")
    else:
        if number_2 > number_3:
            print(f"The greatest number in range is {number_2}")
        else:
            print(f"The greatest number in range is {number_3}")


max_of_three(num1, num2, num3)
