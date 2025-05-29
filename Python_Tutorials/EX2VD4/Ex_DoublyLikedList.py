class Node:

    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:

    def __init__(self):
        self.head = None 
        self.end = None

    def insert_At_Begining(self, data):
        node = Node(data, None, None)
        if(not self.head): # CASE WHERE LINKED LIST IS EMPTY
            self.head = node
        else: # CASE WHERE LINKED LIST HAS ELEMENTS
            self.head.prev = node
            node.next = self.head
            self.head = node

    def getLength(self):
        count = 0
        itr = self.head
        while itr.next:
            count = count + 1
            itr = itr.next
        print(count + 1)
        return count + 1

    def print_LinkedList_Forward(self):
        if(self.head == None):
            raise Exception("Linked list does not exist")
        llstr = ""
        itr = self.head
        while itr:
            llstr = llstr + str(itr.data) + "--->"
            itr = itr.next
        print(llstr)

    def print_LinkedList_Backward(self):
        if(self.head == None):
            raise Exception("Linked list does not exist")

        llstr = ""
        itr = self.head
        lastnode = None
        while itr.next:
            itr = itr.next

        print(str(itr.data) + " This is the last node")
        while itr:
            llstr = llstr + str(itr.data) + "<---"
            itr = itr.prev

        print(llstr)        

    def insert_At_End(self, data):
        node = Node(data, None, None)
        if(self.head == None):
            self.head = node
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = node
            node.prev = itr


if __name__ == "__main__":
    Dll = DoublyLinkedList()
    Dll.insert_At_Begining("Ragi Janardhan")
    Dll.print_LinkedList_Forward()
    Dll.insert_At_Begining("Ragi Vinay Kumar")
    Dll.insert_At_End("Karthik Ragi")
    Dll.print_LinkedList_Forward()
    Dll.print_LinkedList_Backward()
    Dll.getLength()
