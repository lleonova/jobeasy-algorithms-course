# Find the maximal sequence of consecutive zeros that surrounded by ones
# at both ends in the binary representation of a number entered by User.

# n = int(input('Input a number '))
#
#
# def to_bin(number):
#     bin_string = ''
#     while number > 0:
#         bin_string += str(number % 2)
#         number = number // 2
#     return bin_string[::-1]
#
# # 100011100000101000000000
# print(f'binary number {to_bin(n)}')
# print(f'binary number from bin function {bin(n)}')
# def binary_gap(bin_number):
#     max_gap = 0
#     counter = 0
#
#     for digit in bin_number:
#         if digit == '1':
#             if max_gap < counter:
#                 max_gap = counter
#             counter = 0
#         else:
#             counter += 1
#     print(max_gap)
#
#
# binary_gap(to_bin(n))


print(bin(13))
print(bin(13)[2:])