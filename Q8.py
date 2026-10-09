"""
Take two numbers as input. Print the greater of the two. If they are
equal, print "Both are equal.
"""

a = int(input("Enter the First Number: "))
b = int(input("Enter the Second Number: "))

if a > b:
    print(f"{a} is Greater than {b}")
elif a < b:
    print(f"{b} is Greater than {a}")
else:
    print(f"Both are equal")
