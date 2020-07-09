# When given a list, the program should return a list of all the elements
# that are below the arithmetical mean of the original list.
# The arithmetical mean is the sum of all elements divided by the number of elements.

def below_arithmetical_mean (list):

    mean = sum(list) / len(list)
    print(f'Arithmetical mean of this list is: {mean}')
    new_list = []
    for number in list:
        if number < mean:
            new_list.append(number)
    return new_list


print('New list is:', below_arithmetical_mean([4,5,5,6,4,3,2,1,4]))