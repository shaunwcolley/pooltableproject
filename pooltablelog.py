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

def show_table_cost(array):
    for i in range(0, len(array)):
        table = array[i]
        item_number = table.number
        status = table.status_return()
        if table.is_available() == False:
            table.cost_calc()
            print(f"Table {item_number} - {status} - {table.hours_rented()} hours and {table.min_rented()} minutes, current cost is ${table.cost}")


def show_menu():
    print("Enter 1 to view all tables.")
    print("Enter 2 to rent out table.")
    print("Enter 3 to view current cost of tables rented out.")
    print("Enter 4 to close out table.")
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

def close_out_table(array):
    try:
        selection = int(input("Please enter table number to close: ")) - 1
        table = array[selection]
        if table.is_occupied:
            table.close_table()
            time = table.end_time.strftime("%I:%M %p")
            print(f"Table {table.number} closed at {time}, total cost is ${table.cost}")
            table.reset_cost()
        else:
            print(f"Table {table.number} is not currently rented out.")
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

def convert_to_object(array):
    new_array = []
    for item in array:
        number = item["Number"]
        table = PoolTable(number)
        table.start_time = datetime.strptime(item["Start Date Time"], "%Y-%m-%d %H:%M:%S.%f")
        table.end_time = datetime.strptime(item["End Date Time"], "%Y-%m-%d %H:%M:%S.%f")
        table.total_minutes = item["Total Minutes Played"]
        table.cost = item["Total Cost"]
        table.is_occupied = item["Status"]
        new_array.append(table)
    return new_array

def load_tables(a):
    date_today = date.today().strftime("%m-%d-%Y")
    filename = f"{date_today}"
    try:
        with open(filename) as file_object:
            tables = json.load(file_object)
            a = convert_to_object(tables)
            return a
    except FileNotFoundError:
        pass

pooltables = load_tables(pooltables)
if pooltables == None:
    pooltables = []
    add_12_tables(pooltables)

while user_input != "q":
    show_menu()
    user_input = input(">> ")
    if user_input == "1":
        show_tables(pooltables)
    elif user_input == "2":
        show_tables(pooltables)
        rent_out_table(pooltables)
    elif user_input == "3":
        show_table_cost(pooltables)
    elif user_input == "4":
        show_tables(pooltables)
        close_out_table(pooltables)
    elif user_input == "q":
        convert_objects(pooltables, pooltables_dictionaries)
        save_tables(pooltables_dictionaries)
    else:
        print("Please enter a valid input.")
