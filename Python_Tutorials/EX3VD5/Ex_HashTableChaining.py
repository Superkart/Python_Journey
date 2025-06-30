class HashTable:

    def __init__(self):
        self.MAX = 100
        self.arr = [[] for ele in range(self.MAX)]

    def get_Hash(self, key):
        h = 0
        for char in key:
            h = h + ord(char)

        return h % self.MAX
    
    def __setitem__(self, key, value):
        h = self.get_Hash(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                # CASE 1 key is there
                self.arr[h][index] = (key, value)
                found = True
                break
            # CASE 2 key is not there                   ################## needs to be outside the loop  #############
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_Hash(key)
        for keyValue in self.arr[h]:
            if(keyValue[0] == key):
                return keyValue[1]
    
    def __delitem__(self, key):
        h = self.get_Hash(key)
        for index, keyValue in enumerate(self.arr[h]):
            if(keyValue is not None and keyValue[0] == key):
                del self.arr[h][index]


                
            


if __name__ == '__main__':
    ht = HashTable()
    ht["Vinay Kumar Ragi"] = 53
    ht["Karthik Ragi"] = 26
    ht["Madhavi Ragi"] = 52
    ht["Ragi Madhavi"] = 53

    ht["march 17"] = 17
    ht["march 6"] = 6
    print(ht.arr)
    del ht["Madhavi Ragi"]
    print(ht.arr)
    print(ht["MadhaviRagi"])
