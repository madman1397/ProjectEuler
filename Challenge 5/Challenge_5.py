# The following problem is taken from Project Euler: 
#
# ---Smallest Multiple---
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is EVENLY DIVISIBLE by all the numbers from 1 to 20?

def gcd(a, b):
    while b:
        a, b = b, a % b
    print(a)
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def smallestMultiple(n):
    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)
    return result

if __name__ == "__main__":
    r = 20
    result = smallestMultiple(r)
    print(f"The smallest number divisible by 1 through {r} is: {result}")
