"""
. Write a lambda function that takes a number and returns "Positive", or
          "Negative"
"""

positive_or_negative = lambda num: "Positive Number" if num > 0 else "Negative Number"
num1 = int(input("Enter the Number: "))
print(positive_or_negative(num1))
