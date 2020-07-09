# When given a list of elements
# find the two lowest elements.
# They can be equal to each other or different.

def two_lowest_elements(list):
    lowest = list[0]
    prewious_lowest = list[0]
    for number in list:
        if number < lowest:
            prewious_lowest = lowest
            lowest = number
    return lowest, prewious_lowest

print(two_lowest_elements([1,3,6,2,0,4,7,5]))