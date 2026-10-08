"""
Take the user's age as input. Check and print whether they are eligible
to vote (age >= 18) and whether they are a senior citizen (age >= 60).
Print both results.
"""

age = int(input("Enter the Age: "))
if age < 18:
    print("You are not Eligible for Vote")
elif age >= 18 and age <= 59:
    print("You ate Elgible for Vote ")
else:
    print("You ate Senior Citizen")
