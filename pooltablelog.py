import json
from datetime import datetime, time
from pool_table import PoolTable

pooltables = []
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
    selection = int(input("Please enter table number to rent: ")) - 1
    table = array[selection]
    if table.is_available():
        table.rent_table()
        time = table.start_time.strftime("%I:%M %p")
        print(f"Table {table.number} rented out at {time}.")
    else:
        print(f"Pool Table {selection} is currently occupied.\n")

add_12_tables(pooltables)


while user_input != "q":
    show_menu()
    user_input = input(">> ")
    if user_input == "1":
        show_tables(pooltables)
    if user_input == "2":
        show_tables(pooltables)
        rent_out_table(pooltables)
