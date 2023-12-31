# The following problem is taken from Project Euler: https://projecteuler.net/problem=1
# 
# ---Multiples of 3 or 5---
# If we list all the natural numbers (positive integers) below 10 that are multiples of 3 or 5,
# we get 3,5,6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000

def main():
    multiples = []
    for i in range(1,1000):
        if i%3 == 0 or i%5 == 0:
            multiples.append(i)

    print(f"the sum of all multiples of 3 and 5 below 1000 is {sum(multiples)}")

if __name__ == '__main__':
    main()