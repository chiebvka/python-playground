"""
Lecture: Intro to OOP
Exercise: Restuarant Booking 1

"""

restaurant = {"table1": {"seats": 4, "bookings": [{"time": 10, "name": "Chris", "people": 4},
                                                  {"time": 12, "name": "Janet", "people": 3},
                                                  {"time": 14, "name": "Sarah", "people": 2},
                                                  {"time": 16, "name": "Amanda", "people": 4}]},
              "table2": {"seats": 6, "bookings": [{"time": 8, "name": "Sandra", "people": 6},
                                                  {"time": 10, "name": "Antonio", "people": 5},
                                                  {"time": 14, "name": "Chen", "people": 3},
                                                  {"time": 16, "name": "Klaus", "people": 5}]},
              "table3": {"seats": 2, "bookings": [{"time": 10, "name": "Suzuki", "people": 2},
                                                  {"time": 14, "name": "Bruce", "people": 1}]}}

# This code doesn't validate the input
def main():
    while True:
        #Read in the table name that the person wants to book.
        table = input("\nEnter the table name: ")

        #If the table exists in the restaurant
        if table in restaurant:
            #get the time and check for the bookings at that time.
            time = input("Enter the time: ")
            client = ""
            for reservation in restaurant[table]["bookings"]:
                if reservation["time"] == int(time):
                    client = reservation["name"]

            print(f"{table} has {restaurant[table]['seats']} seats.")
            print(f"At that time that table is reserved for: {client}")
        else:
            print("Table not found.")

if __name__ == "__main__":
    main()
