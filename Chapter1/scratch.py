# Cracking the Code interview
# Interview question 1.1
# Algorithm to determine if string has all unique characters

def isUnique(inStr):
    # Assume ASCII chars
    if len(inStr) > 256:
        return False

    # set 128 values to false
    charNums = 128 * [False]

    # cycle through numbers
    for i in range(0, len(inStr)):

        val = ord(inStr[i])

        if charNums[val]:
            return False

        charNums[val] = True

    return True

if __name__ == '__main__':
    if isUnique('abcd'):
        print("Yea budd")
    if not isUnique('abcc'):
        print("cheese")

