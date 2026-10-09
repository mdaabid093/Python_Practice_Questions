"""
Take a person's age and whether they have a valid ID (True/False) as input. They
can enter a venue only if they are 18 or older AND have a valid ID. Print the
appropriate message
"""

age = int(input("Enter Your Age: "))
valid_id = input("Do you have Valid_ID: ")

if age >= 18 and valid_id == True:
    print("You can Enter in a Venue:")
else:
    print("You cannot enter in a Venue")
