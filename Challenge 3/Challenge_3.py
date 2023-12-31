# The following problem is taken from Project Euler: 
#
# ---Largest Prime Factor---
# The prime factors of 13195 are 5,7,13, and 29.
#
# What is the largest prime factor of the number 600851475143?

def LPF(n): #Largest Prime Factor
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

def main():
    largestPrime = LPF(600851475143)
    print(largestPrime)

if __name__ == "__main__":
    main()