# Find and replace a substring in a string for another substring.
# User enter from a keyboard a string and both substrings.
# DON’T USE METHOD REPLACE

def replasing_substring_in_the_string(string, substring1, substring2):
    index = 0
    result_string = ""

    if len(substring1) > len(string):
        return("Substring is too big")

    elif len(substring1) == 0 or len(string) == 0:
        return("String is empty")

    while index <= len(string)-1:

        if substring1 == string[index:len(substring1)+ index]:
            result_string = result_string + substring2
            index += len(substring1)
        else:
            result_string = result_string + string[index]
            index += 1

    return(result_string)


s1 = input("please enter a string of characters:")
s2 = input("please enter a substring of characters:")
s3 = input("Please enter another substring of the caracters:")\

print(replasing_substring_in_the_string(s1, s2, s3))