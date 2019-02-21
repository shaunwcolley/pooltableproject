from datetime import datetime, time

class PoolTable:
    def __init__ (self, number):
        self.number = number
        self.is_occupied = False
        self.start_time = datetime.now()
        self.end_time = datetime.now()
        self.total_minutes = 0
        self.times_played = 0

    def rent_table(self):
        self.is_occupied = True
        self.start_time = datetime.now()
        self.times_played += 1

    def close_table(self):
        self.is_occupied = False
        self.end_time = datetime.now()
        

    def is_available(self):
        if self.is_occupied == True:
            return False
        else:
            return True

    def hours_rented(self):
        start_hour = float(self.start_time.strftime("%H"))
        now = datetime.now()
        current_hour = float(now.strftime("%H"))
        hours_rented =  current_hour - start_hour
        return hours_rented

    def min_rented(self):
        start_min = float(self.start_time.strftime("%M"))
        now = datetime.now()
        current_min = float(now.strftime("%M"))
        min_rented =  abs(current_min - start_min)
        return min_rented

    def total_min_rented(self):
        self.total_minutes += (self.hours_rented() * 60) + self.min_rented()
        return self.total_minutes

    def status_return(self):
        if self.is_occupied == True:
            return "Occupied"
        else:
            return "Unoccupied"

    def to_dictionary(self):
        return {"Number": self.number,
        "Start Date Time": str(self.start_time),
        "End Date Time": str(self.end_time),
        "Total Minutes Played": self.total_min_rented()}
