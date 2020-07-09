# Given the triangle of consecutive odd numbers:
#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:
#
# row_sum_odd_numbers(1); # 1
# row_sum_odd_numbers(2); # 3 + 5 = 8
# row_sum_odd_numbers(3); # 7 + 9 + 11 = 27
# row_sum_odd_numbers(4); # 13 + 15 + 17 + 19 = 64

# First version:
def sum_odd_numbers (index):
    return index ** 3

#Second version:
def sum_odd_numbers_1 (index):
    # First number:
    n = index ** 2 - index + 1
    summ= 0
    i = 0
    while i < index:
        summ = n + summ
        i += 1
        n += 2
    return summ

print(sum_odd_numbers(2))
print(sum_odd_numbers_1(2))