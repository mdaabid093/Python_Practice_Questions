"""
Question 57: Check if a List is Sorted
Write a program that takes a list of numbers and, using a loop, determines whether it is sorted in ascending order. Print True if it is sorted, and False otherwise.
Do not use built-in sort or sorted() functions for checking.
# Example 1:
# numbers = [1, 5, 10, 15, 20]
# Expected Output: True
# Example 2:
# numbers = [1, 10, 5, 15, 20]
# Expected Output: False
# Example 3:
# numbers = []
# Expected Output: True (An empty list is considered sorted

"""


def is_sorted(lst):
    n = len(my_list)
    for i in range(0, n - 1):
        if my_list[i] > my_list[i + 1]:
            return False
    return True


my_list = [3, 5, 7, 9, 10]
print(is_sorted(my_list))
