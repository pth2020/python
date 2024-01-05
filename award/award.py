#This is a Python program that uses if-elif-else statements.
#A user inputs individual times in minutes for a triathlon 
#(swimming,cycling and running) competition.
#The program adds all times and outputs total time taken and 
#the type of award the user gets accordingly.

print("Welcome to the triathlon award ceremony!")
print()

#initialising variables
valid_time_input = False
total_time = 0

#Competitor inputs their time for swimming, cycling and running (in minutes)
time_swimming = int(input("Enter your total time for swimming in minutes: "))
time_cycling = int(input("Enter your total time for cycling in minutes: "))
time_running = int(input("Enter your total time for running in minutes: "))

#checking for validity of inputs
if time_swimming > 0 and time_cycling > 0 and time_running > 0:
    valid_time_input = True
    total_time = time_swimming + time_cycling + time_running
else:
    print("You have entered invalid time")


if valid_time_input:
    print("\nWorking out your award...") 
    print(f"Your total time for the triathlon is {total_time} minutes.")

    if total_time > 0 and total_time <= 100:  
        print("Your award is Provincial Colours.") 
    elif total_time >= 101 and total_time <= 105:
        print("Your award is Provincial Half Colours.")
    elif total_time >= 106 and total_time <= 110:
        print("Your award is Provincial Scroll.")
    else:
        print("Unfortunately, you will not get any award.")
