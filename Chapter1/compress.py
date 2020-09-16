# Cracking the Code interview
# Interview question 1.5
# Compress string aaaaabbbbccc to a5b4c3 only output if len it less than orig string

def compress(string1):

    newStr = ''
    count = 1

    for i in range(0, len(string1)):
        # Check for end of string
        if i+1 < len(string1):
            # Compare current letter to next
            if string1[i] == string1[i+1]:
                # Match, Increment count
                count += 1
            else:
                # No match, add to new string, reset count
                newStr += string1[i] + str(count)
                count = 1
        else:
            # End of string, add letter and count to new string
            newStr += string1[i] + str(count)
            # Compare length
            if len(string1) < len(newStr):
                # Original string smaller, return that
                return string1
            # New String smaller
            return newStr

if __name__ == '__main__':
    print(compress('aaaaaaabbbbbccvvv'))
    print(compress('abc'))