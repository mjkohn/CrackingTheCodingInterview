# Cracking The Coding Interview
# File that will generate linked lists and other support functions

class Node(object):
    def __init__(self, next=None, data=None):
        self.next = next
        self.data = data

class LinkedList(object):
    def __init__(self):
        self.head = None