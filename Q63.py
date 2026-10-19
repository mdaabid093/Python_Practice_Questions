"""
Question 63
Create a list containing the squares of numbers
from 1 to 10 (i.e., [1, 4, 9, ..., 100]).
# Expected output:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100
"""


def square():
    lst = []
    num = 0
    for i in range(1, 101):
        num = i * i
        lst.append(num)
    print(lst)


square()
