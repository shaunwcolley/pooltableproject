import json
from datetime import date
from pool_table import *

#def save_tables(array):
#    a = date.today()
#    date_today = a.strftime("%m-%d-%Y")
#    filename = f"{date_today}"
#    with open(filename, "w") as file_object:
#        json.dump(array, file_object)

#table = PoolTable(1)
#table_dict = table.to_dictionary()

#dictionaries = []
#dictionaries.append(table_dict)

#save_tables(dictionaries)

a = date.today()
date_today = a.strftime("%m-%d-%Y")
filename = f"{date_today}"

#with open(filename) as file_object:
#  dictionaries = json.load(file_object)
pooltables = []
def add_12_tables(array):
    for i in range(0,12):
        table_number = i + 1
        pooltable = PoolTable(table_number)
        array.append(pooltable)




#add_12_tables(pooltables)
pooltables = load_tables(pooltables)
for item in pooltables:
    print(item.number)




#with open(filename) as file_object:
#    if json.load(file_object)
