import pandas as pd

df = pd.read_excel("D:\MyPersonalProjects\Python_Journey\Python_Tutorials\EX3VD5\KarthikGrades_Uic.xlsx")

course_dict = {}
for index, row in df.iterrows():
    key = row["Course Code"]
    value = row.drop("Course Code").to_dict()
    course_dict[key] = value

#print(course_dict)
print(course_dict["CS426"])


class HashTable:

    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

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

hp = HashTable()
hp["CS524"] = "Data Visualization"
hp["CS418"] = "Introduction to Data Science"
print(hp["CS524"])
print(hp.arr)



