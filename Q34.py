"""
1 0 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 0 1

"""

for i in range(1, 6):
    for j in range(1, -1, -1):
        print(j, end=" ")
    for j in range(1, -1, -1):
        print(j, end=" ")
    for j in range(1, -0, -1):
        print(j, end=" ")
    print()
