"""
Take numbers as input from the user one by one. Skip negative
numbers and keep adding the positive ones. Stop when the user
enters 0 and print the total. (Uses both continue and break.
"""

total = 0
i = 1
while True:
    num = int(input("Enter the Number: "))
    if num < 0:
        continue

    elif num == 0:
        break
    else:
        total += num

    i += 1
print(total)
