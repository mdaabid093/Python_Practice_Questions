"""
Create a list of numbers (e.g., [5, 2, 8, 1, 9, 3]). Print the list in ascending order and then in descending order using the sorted() function.
After printing, verify and print the original list to confirm it remains unchanged.
# Expected Output (using hypothetical list):
# Ascending Order: [1, 2, 3, 5, 8, 9]
# Descending Order: [9, 8, 5, 3, 2, 1]
# Original List: [5, 2, 8, 1, 9, 3
"""

my_List = [5, 2, 8, 1, 9, 3]
secomd_list = sorted(my_List)
print(f"Ascending Order:{secomd_list}")
print(f"Decending Order:{secomd_list[::-1]}")
print(f"Original List:{my_List}")
