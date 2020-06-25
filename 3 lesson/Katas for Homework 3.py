# I’s 8 kyu Kata, first in the list of Katas, organized by simplicity - the most simple one :)
# I’ve spend more than 8 hours on it :)

# 1. Given a string s, write a method (function) that will return true
# if its a valid single integer or floating number or false if its not.
#
# Valid examples, should return true:
# isDigit("3")
# isDigit("  3  ")
# isDigit("-3.23")
#
# should return false:
# isDigit("3-4")
# isDigit("  3   5")
# isDigit("3 5")
# isDigit("zero")


# Using algorithms took me a while.
# this programm passed 109 tests from 110 :)
# They don't show which test is failed.
# After lot of recech on-line I think I've missed the floating numbers with "e" instead of point.

def is_this_a_number(string):
    dots = 0                                # variable to count dots
    space_index_front = 0                   # variable to remove spases from the front
    space_index_back = len(string) - 1      # variable to remove spases from the back
    count_of_numbers = 0

# empty string returns false
    if string == "":
        return False
# counting empty spases from the front
    while space_index_front < len(string) and string[space_index_front]  == " ":
            space_index_front += 1
# string with only spases returns false
    if space_index_front == len(string):
            return False
# counting empty spases from the back
    while string[space_index_back] == " ":
            space_index_back -= 1

# checking characters
    for char in str(string[space_index_front:space_index_back]):
        # not number returns false
        if char not in "0123456789-.":
            return False
        # minus should only be first, otherwise - false
        elif char == "-":
                if string.index("-") != space_index_front:
                    return False
                else:
                    if string[space_index_front:space_index_back].count("-") > 1:
                        return False
        # count dots and numbers
        elif char == ".":
            dots += 1
        elif char in "0123456789":
            count_of_numbers += 1
    # more than one dot returns false
    if dots > 1:
        return False
    # string without numbers returns false
    if count_of_numbers == 0:
        return False

    else: return True

print(is_this_a_number("  -12.5     "))

# After more resect on-line I’ve come up with this code, using functions :)

def is_this_a_number2(string):

    try:
        if type(float(string)) is float:
            return True
        return False
    except ValueError:
        return False

print(is_this_a_number2("     -123e5    "))



#----------------------------
# 2. Remove all exclamation marks from the end of sentence.
# Examples:
# remove("Hi!") === "Hi"
# remove("Hi!!!") === "Hi"
# remove("!Hi") === "!Hi"
# remove("!Hi!") === "!Hi"
# remove("Hi! Hi!") === "Hi! Hi"
# remove("Hi") === "Hi"


def remove(s):
    index = len(s) - 1
    while s[index] == '!':
        index = index - 1
    return s[:index + 1]

print(remove("!hi!!"))


def remove_1(s):
    return(s.rstrip("!"))

print(remove_1("!hi!!"))

#-----------------------------
# 3. Write function isItLetter which tells us if given character is a letter.

def IsItLetter(char):
    if char.lower() in "abcdefghigklmnopqrstuvwxyz":
        return True
    else: return False

print(IsItLetter(" "))