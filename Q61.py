"""
Question 61
Given a list, remove all duplicate elements while
preserving the original order of the unique items.
# Example input:
data = [10, 20, 30, 20, 10, 40, 50, 40]
# Expected output: [10, 20, 30, 40, 50
"""


def remove_Duplicate(my_lst):
    lst = []
    for i in my_lst:
        if i not in lst:
            lst.append(i)
    print(lst)


my_lst = [3, 5, 2, 3, 22, 44, 3]
remove_Duplicate(my_lst)
