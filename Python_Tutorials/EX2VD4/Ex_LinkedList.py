class Node:
    
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    
    def insert_At_Begining(self, data):
        node = Node(data, self.head)
        self.head = node
        

    def printLinkedList(self):
        if self.head == None:
            print("Linked list does not exist")
            return
        
        itr = self.head
        llstr = ""

        while itr:
            llstr = llstr + str(itr.data) + " --->"
            itr = itr.next

        print(llstr)


    def insert_At_End(self, data):
        if self.head is None: # CASE WHEN THE LINKED LIST IS EMPTY
            self.head = Node(data, None)
            return
        itr = self.head # GENERAL CASE
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)


    def insert_By_Values(self, data_list):
        self.head = None 
        for data in data_list:
            self.insert_At_End(data)


    def insert_After_Value(self, data_after, data_to_insert):
        
        if(self.head == None):
            raise Exception("Linkedlist doesnt exist")
        
        itr = self.head
        
        while itr:
            if(itr.data == data_after):
                node = Node(data_to_insert, itr.next)
                itr.next = node
                return
            itr = itr.next

        raise Exception("Value not found")      
    







    def remove_Node(self, index):
        if(index < 0 or index >= self.get_Length()): # CASE WHEN INDEX IS NOT IN THE LINKEDLIST
            raise Exception("Invalid index")
        
        if(index == 0): # CASE WHEN INDEX IS THE FIRST ELEMENT
            self.head = self.head.next

        count = 0 # GENERAL CASE 
        itr = self.head
        while itr:
            if(count == index - 1):
                itr.next = itr.next.next
                break

            itr = itr.next
            count = count + 1




if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_By_Values(["Ragi Janardhan", "Ragi Vinay Kumar", "Ragi Karthik"])
    ll.insert_After_Value("Ragi Karthik", "After Karthik")
    ll.printLinkedList()    