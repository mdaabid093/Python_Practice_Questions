"""
        5
      5 4
    5 4 3
  5 4 3 2
5 4 3 2 1
"""

for i in range(1, 6):
    for k in range(1, 6 - i):
        print(" ", end=" ")
    for j in range(5, 5 - i, -1):
        print(j, end=" ")
    print()
