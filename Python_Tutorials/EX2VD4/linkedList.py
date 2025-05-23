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
        
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_At_Begining(5)
    ll.insert_At_Begining(89)
    ll.printLinkedList()
