"""
Question 55: Calculate the Average
Given a list of numbers, use a loop to calculate and print their average. You can use len() to get the count of elements, but avoid using sum() for the total.
Format the average to two decimal places.
# Example:
# scores = [85, 90, 78, 92, 88]
# Expected Output: The average score is: 86.60

"""


def calculate_Average(lst):
    total = 0
    for num in scores:
        total = total + num
    return total


scores = [85, 90, 78, 92, 88]
n = len(scores)
sum = calculate_Average(scores)
average = sum / n
print(f"Average Score is:{average:.2f}")
