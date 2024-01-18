"""
Lecture: Intro to OOP
Exercise: Restuarant Booking 2

"""

# list of booking times corresponding to 8, 10, 12, 14 and 16
# each booking is a dict with the tables, the values correspond to:
# seats, name, people
bookings = [{"table2": [6, "Sandra", 6]},  # at 8
            {"table1": [4, "Chris", 4], "table2": [6, "Antonio", 5], "table3": [2, "Suzuki", 2]},  # at 10
            {"table1": [4, "Janet", 3]},  # at 12
            {"table1": [4, "Sarah", 2], "table2": [6, "Chen", 3], "table3": [2, "Bruce", 1]},  # at 14
            {"table1": [4, "Amanda", 4], "table2": [6, "Klaus", 5]}]  # at 16

# This code doesn't validate the input
def main():
    while True:
        # Get the user input
        time = int(input("\nEnter the time (8, 10, 12, 14 or 16): "))
        table = input("Enter the table name: ")

        #Get the booking information to compare
        booking_time = bookings[(time//2)-4]
        seats = booking_time[table][0]
        client = booking_time[table][1]

        #Just book it - this can be replaced with a proper check
        print(f"{table} has {seats} seats.")
        print(f"At that time that table is reserved for: {client}")

if __name__ == "__main__":
    main()
