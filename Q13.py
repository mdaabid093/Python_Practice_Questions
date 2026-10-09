"""
Take a number as input. Using the ternary operator, print "Even" or "Odd" in a single line
"""

num = int(input("Enter a Number: "))
a = "Even" if num % 2 == 0 else "Odd"
print(a)
