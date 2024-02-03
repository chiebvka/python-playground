from dataannotation import Customer
# from table import table

class Reservation(object):
    
    def __init__(self, date_time, customer, table, people):
        self.__date_time = date_time
        self.__customer = customer
        self.__table = table
        self.__num_people = people

    # get_day() :String - return a string that is


    def get_name(self):
        return
    
    # def get_phone(self):
    #     String - return the phone number of the customer

    # def get_table(self):
    #     String - return table identifier