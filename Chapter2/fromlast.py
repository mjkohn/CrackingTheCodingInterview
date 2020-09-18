# Cracking The Coding Interview
# File that will generate linked lists and other support functions
# 2.2 find kth from end element

from Chapter2 import LinkedList as ll


def kthfromend(LL, value):
    length = LL.getLength()

    if value > length:
        print("Error: Kth from end element {} is outside linked list length {}".format(value, length))
        return None

    current = LL.head
    count = 0

    while current:
        if count == (length - count):
            return current
        count += 1
        current = current.next

    return None


if __name__ == '__main__':
    LL = ll.LinkedList()
    LL.insert(3)
    LL.insert(4)
    LL.insert(5)
    LL.insert(6)
    LL.printLL()
    node = kthfromend(LL,5)
    print("done")