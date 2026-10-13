"""
Create a list of 5 of your favourite movies. Print the first, last, and middle movie from your list using both positive and negative indexing where appropriate
"""

movies_list = ["3Idiots", "KGF", "Bahubali", "Bahubali2", "Pathan"]
print(f"First Movie:{movies_list[0]}")
print(f"Middle Movie:{movies_list[len(movies_list)//2]}")
print(f"Last Movie:{movies_list[len(movies_list)-1]}")
