# Cracking the Code interview
# Interview question 1.2
# Determine if two strings are permutations of eachother

MAX_CHARS = 256

def permute2(string1, string2):

    # Check for same length
    if len(string1) != len(string2):
        return False

    # Initialize count vars - will count ord of values
    count1 = MAX_CHARS * [0]
    count2 = MAX_CHARS * [0]

    for i in string1:
        count1[ord(i)] += 1

    for i in string2:
        count2[ord(i)] += 1

    for i in range(0, MAX_CHARS):
        if count1[i] != count2[i]:
            return False

    return True

if __name__ == '__main__':
    one = 'abc'
    two = 'cab'
    three = 'bada'

    if permute2(one, two):
        print('Matchy Matchy')
    else:
        print('Nope')

    if permute2(two, three):
        print('Two three')
    else:
        print('Not again')