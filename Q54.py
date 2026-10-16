"""
Question 53: Find the Largest Element
Given a list of numbers, write Python code using a loop to find and print the largest element. Do not use the built-in max() function.
# Example:
# numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# Expected Output: The largest element is:9
"""

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
n = len(numbers)
maxi = float("-inf")
for i in numbers:
    if i > maxi:
        maxi = i

print(f"Largest Element is {maxi}")
