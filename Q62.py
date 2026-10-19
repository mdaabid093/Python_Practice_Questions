"""
Question 62
Separate a list of integers into two distinct lists: one
containing all the even numbers and the other
containing all the odd numbers.
# Example input:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected output:
# evens = [2, 4, 6, 8, 10]
# odds = [1, 3, 5, 7, 9
"""


def separate_List(lst):
    # n=len(lst)

    print(f"even= {lst[1::2]}")
    print(f"odd= {lst[::2]}")


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
separate_List(lst)
