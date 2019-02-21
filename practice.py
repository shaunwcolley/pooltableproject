import json
from datetime import date
from pool_table import *

def save_tables(array):

    date = date.today()
    date_today = date.strftime("%m-%d-%Y")
    filename = f"{date_today}"
    with open(filename, "a") as file_object:
        json.dump(array, file_object)
