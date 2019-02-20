from datetime import datetime, time

class PoolTable:
    def __init__ (self, number):
        self.number = number
        self.is_occupied = False
        self.start_time = datetime.now()
        self.end_time = datetime.now

    def rent_table(self):
        self.is_occupied = True
        self.start_time = datetime.now()

    def close_table(self):
        self.is_occupied = False
        self.end_time = datetime.now()
        #time_rented = self.end_time - self.start_time

    def is_available(self):
        if self.is_occupied == True:
            return False
        else:
            return True

    def hours_rented(self):
        start_hour = int(self.start_time.strftime("%H"))
        now = datetime.now()
        current_hour = int(now.strftime("%H"))
        hours_rented =  current_hour - start_hour
        return hours_rented

    def min_rented(self):
        start_min = int(self.start_time.strftime("%M"))
        now = datetime.now()
        current_min = int(now.strftime("%M"))
        min_rented =  current_min - start_min
        return min_rented



    def status_return(self):
        if self.is_occupied == True:
            return "Occupied"
        else:
            return "Unoccupied"
