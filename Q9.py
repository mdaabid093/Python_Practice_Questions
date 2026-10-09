"""
Take a student's marks as input. Print their grade based on this scale:
90 and above → A
75 to 89 → B
60 to 74 → C
40 to 59 → D
Below 40 → F

"""

marks = int(input("Enter the Student Marks Between 0 to 100 : "))
if marks >= 90:
    print("A Grade")
elif marks <= 89 and marks >= 75:
    print("B Grade")
elif marks <= 74 and marks >= 60:
    print("C Grade")
elif marks <= 59 and marks >= 40:
    print("D Grade")
else:
    print("Fail")
