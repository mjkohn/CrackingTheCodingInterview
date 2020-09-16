# Cracking the Code interview
# Interview question 1.8
# substrings check


def isSubstring(string1, string2):
    # check if string is substring
    if string1.find(string2) == -1:
        return False
    else:
        return True


def stringRotation(string1, string2):
    if len(string1) != len(string2):
        return False

    bigString = string1 + string1

    return isSubstring(bigString, string2)


if __name__ == '__main__':
    if isSubstring('Mike is the best', 'Mike'):
        print('Yea, dats right')
    if not isSubstring("Wadesmellslikecheese", "wood"):
        print("wade smells like cheese")

    if stringRotation('holly', 'lyhol'):
        print('Holly we did it!')