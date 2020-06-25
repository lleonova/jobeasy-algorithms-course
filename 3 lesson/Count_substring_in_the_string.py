# Write a Python function, which will count how many times a character (substring)
# is included in a string. DON’T USE METHOD COUNT


def substring_in_the_string(string, substring):
    index = 0
    count = 0

    if len(substring) > len(string):
        return(0)

    elif len(substring) == 0 or len(string) == 0:
        return(0)

    while index <= len(string) - len(substring):
        if substring == string[index:len(substring)+ index]:
            count +=1
        index += 1
    return(count)


s1 = input("please enter a string of characters:")
s2 = input("please enter a substring of characters:")

print(substring_in_the_string(s1, s2))