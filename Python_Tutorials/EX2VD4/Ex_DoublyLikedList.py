class Node:

    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:

    def __init__(self):
        self.head = None 

    def insert_At_Begining(self, data):
        node = Node(data, None, self.head)
        if(self.head):
            self.head = node

    def insert_At_End(self, data, )
