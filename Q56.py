"""
Question 56: Element-wise Sum of Two Lists
Given two lists of the same length, write Python code using a loop to create a new list where each element is the sum of the corresponding elements from both original lists.
# Example:
# list1 = [10, 20, 30, 40]
# list2 = [1, 2, 3, 4]
# Expected Output: [11, 22, 33, 44]
# list_a = [5, 15, 25]
# list_b = [2, 4, 6]
# Expected Output: [7, 19, 31]

"""


def sum_of_two_list(lst1, lst2):
    new_list = []
    n = len(lst1)
    for i in range(0, n):
        sum = list1[i] + list2[i]
        new_list.append(sum)
    return new_list


list1 = [10, 20, 30, 40]
list2 = [1, 2, 3, 4]

print(sum_of_two_list(list1, list2))
