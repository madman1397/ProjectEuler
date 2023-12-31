# The following problem is taken from Project Euler: https://projecteuler.net/problem=9
#
# ---Special Pythagorean Triplet---
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000
# Find the product abc.

def triplet(sum):
    for a in range(1,sum):
        for b in range(1,sum):
            c = (sum -a) - b
            if a < b <c:
                if a**2+b**2 == c**2:
                    print(f"{a}*{b}*{c}=")
                    return a*b*c
    return "no solution found"

if __name__ == "__main__":
    print(triplet(1000))