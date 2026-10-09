"""
Take a number as input. Print whether it is positive, negative, or zero.
"""

n = int(input("Enter the Number: "))
if n > 0:
    print(f"{n} is Positive Number")
elif n == 0:
    print(f"{n} is Zero")
else:
    print(f"{n} is Negative Number")
