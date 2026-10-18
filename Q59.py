"""
Q59. Reverse a list without using the
.reverse() method or list slicing ([::-1]).
Hint: Think about swapping elements from
both ends of the list using a loop.
Example: [1, 2, 3, 4, 5]
→
 [5, 4, 3, 2, 1]
"""


def reverse_lst(lst):
    new_lst = []
    n = len(lst)
    for i in range(n - 1, -1, -1):
        new_lst.append(lst[i])
    print(new_lst)


lst = [4, 1, 5, 8, 9, 6]
reverse_lst(lst)
