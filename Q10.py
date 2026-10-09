"""
Take a year as input. Check if it is a leap year. A year is a leap
year if it is divisible by 4, but not by 100, unless it is also
divisible by 400
"""

year = int(input("Enter the Year: "))
if year % 4 == 0:
    if year % 100 != 0:
        print(f"{year} is leap year")
elif year % 400 == 0:
    print(f"{year} is leap year")

else:
    print(f"{year} is not a leap year")
