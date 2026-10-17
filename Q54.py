"""
Question 54: Check for Target Existence
Write a program that takes a list and a target number. Use a loop to determine if the target number exists in the list. Do not use the in operator.
# Example:
# my_list = [10, 20, 30, 40, 50]
# target = 30
# Expected Output: 30 exists in the list.
# target = 60
# Expected Output: 60 does not exist in the list

"""


def does_Exist(lst, target):
    for num in my_list:
        if num == target:
            return True
    return False


my_list = [10, 20, 30, 40, 50]
target = int(input("Entr the Target: "))
a = does_Exist(my_list, target)
if a == True:
    print(f"{target} exists in the list")
else:
    print(f"{target} does not exists in the list")
