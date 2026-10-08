"""
Take two numbers as input. Without using *, calculate and print their product
using += in a way that adds the first number to itself the
second number of times.
"""

first_number = int(input("Enter the First Number: "))
second_number = int(input("Enter the Second Number: "))

product = 0
for i in range(second_number):
    product = product + first_number

print(f"Product:{product}")
