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

        #print(str(itr.data) + " This is the last node")
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

    def insert_By_Values(self, data_list):
        if not data_list:
            raise Exception("Data list is invalid")
        for data in data_list:
            self.insert_At_End(data)
             
    def insert_After_Value(self, after_value, data):
        if(self.head == None):
            raise Exception("Invalid request")
        
        itr = self.head

        while itr:                        ###################### checking if the next value exists and if does you need to connect its prev too #####################
            if(itr.data == after_value):
                node = Node(data, itr, itr.next)
                if itr.next:
                    itr.next.prev = node
                itr.next = node
                return
            itr= itr.next
        print("Value doesnt exist")


        

if __name__ == "__main__":
    Dll = DoublyLinkedList()
    Dll.insert_By_Values(["Karthik Ragi", "Ragi Vinay Kumar", "Ragi Janardhan"])
    Dll.insert_After_Value("Karthik Ragi", "Divya Ragi")
    #Dll.insert_At_Begining("Ragi Janardhan")
    #Dll.insert_At_Begining("Ragi Vinay Kumar")
    #Dll.insert_At_End("Karthik Ragi")
    Dll.print_LinkedList_Forward()
    Dll.print_LinkedList_Backward()
    Dll.getLength()
