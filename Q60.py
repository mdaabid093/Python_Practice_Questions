"""
Q60. Given two lists, merge them into a
single new list without modifying the
originals.
Hint: Use the + operator or a loop to
combine. Example: list1 = [1, 2], list2 = [3,
4]
→
 merged = [1, 2, 3, 4]

"""


def merged_lst(lst1, lst2):
    new_lst = lst1 + lst2
    print(new_lst)


lst1 = [4, 5, 6, 32]
lst2 = [44, 22, 33, 1, 2]
merged_lst(lst1, lst2)
