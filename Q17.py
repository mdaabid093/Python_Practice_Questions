"""
Sum of all the numbers from 1 to 100 divisible by 2 and 7 Using while loops.
"""

sum = 0
i = 1
while i <= 100:
    if i % 2 == 0 and i % 7 == 0:
        sum += i
    i += 1
print(f"Sum of all no between 1 to 100 which is divisble by 2 and 7 is {sum}")
