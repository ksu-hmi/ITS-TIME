
# Since this is patient information, you must log into the application
import sys
import signal
import time
import os
import webbrowser


print("You must enter your username and password to access the application")

attempts = 0

username = "sunshine"
password = "Pyth0n"

while True:
    usern = input("Enter Username: ")
    userp = input("Enter Password: ")
    attempts += 1
    if attempts == 3:
        print("Too many incorrect attempts. Goodbye")
        break
    else:
        if usern == username and userp == password:
            print("\nAccess Granted. Welcome " + username)
            break
        else:
            print("Incorrect credentials. Try again")
            
sys.exit


#Create Menu for the application

def print_menu():  # Your menu design here
    print()
    print("Welcome to It's Time your pill reminder")
    print()

    option = input("""
            1. Add A Medication
            2. Delete A Medication
            3. Review A Medication
            4. Set an Alarm for Medication
            5. Exit
            """)
    

print_menu()
choice = input("Enter the menu item that you want to do [1-5]: ")
choice = int(choice)
medication_name=["Zyrtec"]

if choice == 1:
    print ("Add A Medication - Function in Progress")
elif choice == 2:
    print ("Delete A Medication - Function in Progress")
        
elif choice == 3:
    print ("Review A Medication - Function in Progress")
        
elif choice == 4:
    print ("Set an Alarm for Medication")

    alarm_HH = input("Enter the hour you want to take the medication: ")
    alarm_MM = input("Enter the minute you want to take the medication: ")

#    print("You want to take " + medication_name + " at " + alarm_HH + ":" + alarm_MM)

    while True:
        now = time.localtime()
        if now.tm_hour == int(alarm_HH) and now.tm_min == int(alarm_MM):
            print("TAKE the medicine NOW!")
        webbrowser.open("https://www.youtube.com/watch?v=2J51Q6pOATk")
        break
    else:
        timeout = 1 - now.tm_min
        print("no alarm")
        

elif choice == 5:
    print ("Thanks for Using. Goodbye")
        
       
else:
        # Any integer inputs other than values 1-5 we print an error message
    print("Not a valid menu item. Enter any key to try again..")
    print_menu()
