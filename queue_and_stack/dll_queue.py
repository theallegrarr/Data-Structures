import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.items = []
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def enqueue(self, value):
        self.items.insert(0, value)
        self.size += 1

    def dequeue(self):
        if self.len() > 0:
            value = self.items[self.len()-1]
            self.items.pop()
            self.size -= 1
            return(value)
        else:
            pass

    def len(self):
        return len(self.items)
