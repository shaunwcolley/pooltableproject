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

with open(filename) as file_object:
  dictionaries = json.load(file_object)

def convert_to_object(array):
    new_array = []
    for item in array:
        number = item["Number"]
        table = PoolTable(number)
        table.start_time = datetime.strptime(item["Start Date Time"], "%Y-%m-%d %H:%M:%S.%f")
        table.end_time = datetime.strptime(item["End Date Time"], "%Y-%m-%d %H:%M:%S.%f")
        table.total_minutes = float(item["Total Minutes Played"])
        new_array.append(table)
    return new_array
array = convert_to_object(dictionaries)
print(array[0].total_minutes)

#with open(filename) as file_object:
#    if json.load(file_object)
