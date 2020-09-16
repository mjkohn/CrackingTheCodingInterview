# Cracking the Code interview
# Interview question 1.4
# Replace all spaces in string with %20

def replaceSpace(string1):
    return string1.replace(" ", "%20")

if __name__ == '__main__':
    string1 = "I am the best"
    print(string1)
    print(replaceSpace(string1))
    string2 = "Mike"
    print(string2)
    print(replaceSpace(string2))