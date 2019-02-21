import json
from datetime import datetime, time, date
from pool_table import PoolTable

pooltables = []
pooltables_dictionaries = []
user_input = ""

def add_12_tables(array):
    for i in range(0,12):
        table_number = i + 1
        pooltable = PoolTable(table_number)
        array.append(pooltable)

def show_tables(array):
    for i in range(0, len(array)):
        table = array[i]
        item_number = table.number
        status = table.status_return()
        if table.is_available() == False:
            print(f"Table {item_number} - {status} - {table.hours_rented()} hours and {table.min_rented()} minutes")
        else:
            print(f"Table {item_number} - {status}")

def show_menu():
    print("Enter 1 to view all tables.")
    print("Enter 2 to rent out table.")
    print("Enter q to quit.")

def rent_out_table(array):
    try:
        selection = int(input("Please enter table number to rent: ")) - 1
        table = array[selection]
        if table.is_available():
            table.rent_table()
            time = table.start_time.strftime("%I:%M %p")
            print(f"Table {table.number} rented out at {time}.")
        else:
            print(f"Pool Table {selection} has been occupied for {table.hours_rented()} hours and {table.min_rented()} minutes.\n")
    except ValueError:
        print("Please enter a valid number when renting one.")
    except:
        print("Sorry, something terrible has happened. Please try another input.")

def convert_objects(array, super):
    for i in range(0, len(array)):
        table = array[i]
        dict_table = table.to_dictionary()
        super.append(dict_table)

def save_tables(array):
    date_today = date.today().strftime("%m-%d-%Y")
    filename = f"{date_today}"
    with open(filename, "w") as file_object:
        json.dump(array, file_object)

add_12_tables(pooltables)

while user_input != "q":
    show_menu()
    user_input = input(">> ")
    if user_input == "1":
        show_tables(pooltables)
    elif user_input == "2":
        show_tables(pooltables)
        rent_out_table(pooltables)
    elif user_input == "q":
        convert_objects(pooltables, pooltables_dictionaries)
        save_tables(pooltables_dictionaries)
    else:
        print("Please enter a valid input.")
