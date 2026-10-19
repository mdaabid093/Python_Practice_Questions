"""
Given a list of marks, use list comprehension to create a new list that contains only the marks that are above 75.
# Example input:
marks = [65, 80, 70, 90, 75, 82, 60]
# Expected output:
# [80, 90, 82]
"""

marks = [65, 80, 70, 90, 75, 82, 60]
new_lst = [i for i in marks if i > 75]
print(new_lst)
