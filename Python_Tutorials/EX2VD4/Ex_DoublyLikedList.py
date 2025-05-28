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

    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count = count + 1
            itr = itr.next
        print(count)
        return count

    def insert_At_End(self, data, )
