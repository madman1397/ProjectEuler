# The following problem is taken from Project Euler: https://projecteuler.net/problem=7
#
# By listing the first six prime numbers: 2,3,5,7,11, and 13, we can see that the 6th prime is 13.
#
# What is the 10,001st prime number?
import math

def nthPrime(n):
    counter = 2
    for i in range(3, n**2, 2):
        k = 1
        while k*k < i:
            k += 2
            if i % k == 0:
               break
        else:
            counter += 1
        if counter == n:
            return i

if __name__ == "__main__":
    print(nthPrime(10001))