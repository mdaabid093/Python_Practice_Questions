"""
Ask a number from the user, print the multiplication table upto 10 Using while  loops
"""

num = int(input("Enter the Number :"))
i = 1
mul = 1
while i <= 10:
    mul = num * i
    print(f"{num} x {i} = {mul}")
    i += 1
