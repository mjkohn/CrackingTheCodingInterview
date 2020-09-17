# Cracking The Coding Interview
# File that will generate linked lists and other support functions

class Node(object):
    def __init__(self, data=None, next=None):
        self.next = next
        self.data = data

class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def printLL(self):
        current = self.head
        while current:
            print(str(current.data))
            current = current.next


if __name__ == '__main__':
    LL = LinkedList()
    LL.insert(3)
    LL.insert(4)
    LL.insert(5)
    LL.insert(6)
    LL.printLL()