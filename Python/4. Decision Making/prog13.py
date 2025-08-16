age = int(input("Enter Your Age: "))
day = input("Enter the day of the Week: ")

if age < 12:
    print("Your Ticket Amount: ", 150)
elif age >= 12 and age <= 18:
    print("Your Ticket Amount: ", 200)
else:
    if day == 'saturday' or day == 'sunday':
        print("Your Ticket Amount: ", 300)
    else:
        print("Your Ticket Amount: ", 250)