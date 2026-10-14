"""
Create a list of 6 hypothetical student marks (e.g., [75, 88, 62, 91, 70, 83]). Using built-in functions, print the highest mark, lowest mark, total sum of marks, and the average mark.
Format the average to two decimal places.
# Expected Output (using hypothetical marks):
# Highest Mark: 91
# Lowest Mark: 62
# Total Marks: 469
# Average Mark: 78.17
"""

my_list = [75, 88, 62, 91, 70, 83]
total = sum(my_list)
highest_marks = max(my_list)
lowest_marks = min(my_list)
average_marks = total / len(my_list)
print(f"Highest Mark: {highest_marks}")
print(f"Lowest Mark:{lowest_marks}")
print(f"Total Marks:{total}")
print(f"Average Mark:{average_marks:.2f}")
