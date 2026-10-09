"""
Ask a number from the user, and print all the factors Using While Loops
"""

num = int(input("Enter the Number: "))
i = 1
fact = 1
while i <= num:
    fact = fact * i
    i += 1

print(f"Factor of {num} is {fact}")
