# The following problem is taken from Project Euler: 
#
# ---Sum Square Difference---
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is,
# 3025 - 385 = 2640
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sumOfSquares(n):
    return sum([i**2 for i in n])

def squareOfSum(n):
    return sum(n)**2

def main(iter):
    nums = [i+1 for i in range(iter)]
    dif = abs(sumOfSquares(nums) - squareOfSum(nums))
    print(dif)
    
if __name__ == "__main__":
    main(100)