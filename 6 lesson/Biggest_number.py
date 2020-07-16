# Find the biggest number in the list (divide and rule)

array_1 = [1,5,3,1,8,5,9]

def biggest_number(array):

    if len(array) == 0:
        return "Empty list"

    if len(array) == 1:
        return array[0]
    #
    # number = biggest_number(array[1:])
    #
    # if array[0] < number:
    #     array[0] = number
    # return array[0]

    return max(array[0], biggest_number(array[1:]))

print(biggest_number(array_1))


