"""
Write a function called min_of_three that takes three numbers and returns
          the smallest without using any built-in function
"""


def min_of_three(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    return c


num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the Second Number: "))
num3 = int(input("Enter the Third Number: "))
k = min_of_three(num1, num2, num3)
print(f"Smallest Number is {k}")
