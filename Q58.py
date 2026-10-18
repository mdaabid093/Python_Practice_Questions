"""
Q58. Find the largest and smallest number
in a list without using built-in functions like
max() or min().
Hint: Use a loop and a variable to track the
current largest/smallest as you go through
the list. Example: if the list is [3, 1, 4, 1, 5],
the largest is 5 and smallest is 1

"""


def samllest_and_largerst(lst):
    max = float("-inf")
    small = lst[0]
    n = len(lst)
    for i in lst:
        if i > max:
            max = i
    for i in lst:
        if i < small:
            small = i

    return print(f"Largest is {max} and Smallest is {small}")


lst = [3, 5, 1, 33, 55, 99, 4, 3]
samllest_and_largerst(lst)
