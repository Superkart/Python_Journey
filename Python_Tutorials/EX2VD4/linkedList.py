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

    def print_LinkedList(self):
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

    def insert_By_Values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_At_End(data)
            


    

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_By_Values(["Ragi Janardhan", "Ragi Vinay Kumar", "Ragi Karthik"])
    ll.print_LinkedList()
