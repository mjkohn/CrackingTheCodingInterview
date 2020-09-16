# Cracking the Code interview
# Interview question 1.2
# Determine if two strings are permutations of eachother

from itertools import permutations

def permute(string1, string2):
    # get lengths
    len1 = len(string1)
    len2 = len(string2)

    # return false if lengths are different
    if len1 != len2:
        print('Length Fail')
        return False

    # Sort the strings
    sorted1 = sorted(string1)
    sorted2 = sorted(string2)

    # Compare sorted stings
    for i in range(0, len1):
        if sorted1[i] != sorted2[i]:
            return False

    return True

if __name__ =='__main__':
    one = 'abc'
    two = 'cab'
    three = 'bada'

    if permute(one, two):
        print('Matchy Matchy')
    else:
        print('Nope')

    if permute(two, three):
        print('Two three')
    else:
        print('Not again')