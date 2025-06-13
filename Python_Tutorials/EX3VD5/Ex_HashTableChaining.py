class HashTable:

    def __init__(self):
        self.MAX = 100
        self.arr = [None for ele in range(self.MAX)]

    def get_Hash(self, key):
        h = 0
        for char in key:
            h = h + ord(char)

        return h % self.MAX
    
    def __setitem__(self, key, value):
        h = self.get_Hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.get_Hash(key)
        return self.arr[h]
    
    def __delitem__(self, key):
        h = self.get_Hash(key)
        self.arr[h] = None