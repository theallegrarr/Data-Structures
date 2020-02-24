import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.items = []
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def push(self, value):
        self.items.append(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            value = self.items[self.size - 1]
            self.items.pop()
            self.size -= 1
            return value
        else:
            return None

    def len(self):
        return self.size
