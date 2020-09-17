# Cracking The Coding Interview
# File that will generate linked lists and other support functions
# 2.1 remove dupes from linked list

from Chapter2 import LinkedList as ll


def removedupes(LL):
    # Set previous and current
    previous = LL.head
    current = previous.next
    # Set to store data seen
    keys = {previous.data}
    # go through linked list
    while current:
        if current.data in keys:
            # Data found in set, remove node
            previous.next = current.next
            current = current.next
        else:
            # Data not found in set, add data to set
            keys.add(current.data)
            # Increment pointers
            previous = current
            current = current.next


if __name__ == '__main__':
    LL = ll.LinkedList()
    LL.insert(3)
    LL.insert(3)
    LL.insert(4)
    LL.insert(5)
    LL.insert(6)
    LL.insert(5)
    LL.insert(6)
    print("Before\n")
    LL.printLL()
    removedupes(LL)
    print("\nAfter\n")
    LL.printLL()