from Ex_HashTableChaining import HashTable
from pathlib import Path
import pandas as pd


current_File_Path = Path(__file__)
project_Root_Path = current_File_Path.parent
csv_File_Path =  project_Root_Path / "nyc_weather.csv"

df = pd.read_csv(csv_File_Path)

temp_List = df["temperature(F)"].to_list()

print(temp_List)

""""
sum = 0
for temp in range(7):
    sum = sum + temp_List[temp]

week_Avg = sum/7
"""

# BETTER WAY TO DO IT

week_Avg = sum(temp_List[0:7]) / len(temp_List[0:7]) 
               
print(week_Avg)

sorted_Temp_List = sorted(temp_List, reverse=True)

print(sorted_Temp_List[0])