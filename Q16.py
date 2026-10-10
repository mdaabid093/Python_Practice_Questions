"""
Sum of all the numbers from 1 to 100 Using While loops.
"""

i = 1
sum = 0
while i <= 100:
    sum = sum + i
    i += 1

print(f"Total sum between 1 to 100 is {sum}")
# Using For Loop
print()
print("Using For Loop")
sum1 = 0
for i in range(1, 101):
    sum1 = sum1 + i
print(sum1)
