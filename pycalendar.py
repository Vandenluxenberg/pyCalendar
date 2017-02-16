#!/usr/bin/python

"""
Python Calendar Project
"""

from time import sleep, strftime

user_name = "Dave"
my_calendar = {}

# Welcome message #

def welcome():
    print "Welcome " + user_name + "."
    print "Opening the calendar..."
    sleep(1)

    print ""
    print "Today is: " + strftime("%A %B %d, %Y")
    print "Current time is: " + strftime("%H:%M:%S")
    print ""
    sleep(1)

# Print the calendar sorted by month/day #

def print_calendar():
    for date in sorted(my_calendar):
        print date + ": " + my_calendar[date] + "\n"

# Main #

def main_calendar():
    running = True

    while running:
        user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit: ").upper()

        if user_choice == "V":  #View calendar
            if len(my_calendar.keys()) < 1:
                sleep(1)
                print "Calendar is empty.\n"
            else:
                print_calendar()

        elif user_choice == "U":  #Update calendar
            date = raw_input("Enter date: ")

            if not date in my_calendar:
                print "No reminder at this date yet. Use Add instead.\n"
                continue
            else:
                update = raw_input("Enter the update: ")
                my_calendar[date] = update
                sleep(1)
                print "Calendar succesfully updated!\n"

        elif user_choice == "A":  #Add to calendar
            date = raw_input("Enter date (MM/DD/YYYY): ")

            if len(date) != 10:
                print "Error. Valid date format = MM/DD/YYYY.\n"

            elif int(date[6:]) < int(strftime("%Y")):
                print "Error. Can't add a date in the past.\n"

            elif date in my_calendar:
                print "Error. Date already exists. Use Update or Delete first.\n"

            else:
                reminder = raw_input("Enter reminder: ")
                my_calendar[date] = reminder
                sleep(1)
                print "Reminder succesfully added to calendar!\n"

        elif user_choice == "D":  #Delete from calendar
            date = raw_input("Enter date: ")

            if not date in my_calendar:
                print "Error. Date doesn't have a reminder yet.\n"
            else:
                my_calendar.pop(date)
                sleep(1)
                print "Reminder succesfully deleted.\n"

        elif user_choice == "X":  #Exit
            print "Goodbye!\n"
            running = False

        else:  #No valid command entered
            print "Not a valid command.\n"

#Run the program

welcome()

main_calendar()

#EOF
