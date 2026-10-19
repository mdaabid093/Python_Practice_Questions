"""
Find the number is prime or not
"""


def is_Prime(num):
    factor = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factor += 1
    if factor == 2:
        return True
    else:
        return False


a = is_Prime(6)


if a == True:
    print("Prime Number")
else:
    print("Not prime")
