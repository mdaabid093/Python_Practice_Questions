"""
Write a function called find_max that takes three numbers as
         parameters and prints the largest one.
"""


def find_max(a, b, c):
    if a > b and a > c:
        print(f"{a} is a Maximum Number: ")
    elif b > a and b > c:
        print(f"{b} is a Maximum Number: ")
    else:
        print(f"{c} is a Maximum Number")


num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the Second Number: "))
num3 = int(input("Enter the Third Number: "))
find_max(num1, num2, num3)
