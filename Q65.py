"""
Question 65
Write a Python script that iterates through a list of integers and
replaces every negative number found in the list with the value 0.
# Example input list:
numbers = [5, -3, 8, -1, 0, -10, 12]
# Expected output: [5, 0, 8, 0, 0, 0, 12
"""


def replace_positve_integer(lst):
    n = len(lst)
    k = 0
    for i in range(0, n):
        if lst[i] < 0:
            lst[i] = 0
    print(lst)


my_lst = [5, -3, 8, -1, 0, -10, 12]
replace_positve_integer(my_lst)
