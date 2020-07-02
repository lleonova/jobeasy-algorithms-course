# Enter a string of words separated by spaces.
# Find the longest word.

def longest_word(string):
    array = string.split(' ')
    result = array[0]
    for item in array:
        if len(item) > len(result):
            result = item
    return result
print(longest_word('vb mama nvbghn bnb hjnuiytrc'))