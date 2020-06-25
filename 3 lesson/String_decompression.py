# Write a function for decompressing string “a4b3c2d”

def decompression(string):

    result = string[0]

    if result in "0123456789":
        return ('Unexpected format')

    counter = ''
    index = 1
    while index <= len(string)-1:
        if string[index] in "0123456789":
            counter = counter + string[index]
            if index == len(string)-1:
                result = result + result[-1] * (int(counter) - 1)
        else:
            if counter == '':
                result = result + string[index]
                print(result)
            else:
                result = result + result[-1] * (int(counter)-1) + string[index]
                counter = ''
        index += 1

    return(result)

print(decompression('s2d31f10n'))

