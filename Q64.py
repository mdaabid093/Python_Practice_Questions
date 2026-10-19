"""
Question 64
Given a list of numbers (which may contain duplicates), write a
Python script that takes an integer as input from the user and
removes all occurrences of that integer from the list.
# Example input list:
my_list = [10, 20, 10, 30, 20, 10, 40]
# If user enters 10, expected output: [20, 30, 20, 40
"""


def remove_Occurence(lst, n):
    for i in lst:
        if n in lst:
            lst.remove(n)
    print(lst)


my_lst = [2, 3, 4, 7, 8, 2, 5, 2]
num = int(input("Enter the Number that you want to remove: "))
remove_Occurence(my_lst, num)
