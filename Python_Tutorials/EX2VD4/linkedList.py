class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_At_Begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def printLinkedList(self):
        if self.head is None:
            print("Linked list is empty")
            return  
        
        itr = self.head
        llstr = ''

        while itr:
            llstr = llstr + str(itr.data) + '--->'
            itr = itr.next

        print(llstr)
    
    def insert_At_End(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)
        

    

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_At_End(5)
    ll.insert_At_End(89)
    ll.insert_At_End(79)
    ll.insert_At_Begining(0)
    ll.printLinkedList()
