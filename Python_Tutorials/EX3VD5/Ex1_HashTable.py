from Ex_HashTableChaining import HashTable
from pathlib import Path
import pandas as pd


current_File_Path = Path(__file__)
project_Root_Path = current_File_Path.parent
csv_File_Path =  project_Root_Path / "nyc_weather.csv"

df = pd.read_csv(csv_File_Path)

print(df.head())