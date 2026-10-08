"""
Take a number as input. Print whether it is even or odd using the %
operator and a comparison operator
"""

a = int(input("Enter the Number: "))
# Using % operator
if a % 2 == 0:
    print(f"{a} is an Even Number")
else:
    print(f"{a} is an Odd Number")

# Using comparison operator
if a / 2 == a // 2:
    print(f"Yes It is an Even number Using Comparison Operator")
else:
    print(f"Yes It is an Odd number Using Comparison Operator")
