# Write a recursive function to count all the elements in a list (divide and rule)

array_1 = [1,2,33,444,5555,6,'a','b','c','d','.','-',0]

def count_elements(array: list):
    count = 0
    if len(array) == 0:
        return count
    else:
        count += 1 + count_elements(array[1:])
    return count

print(count_elements(array_1))