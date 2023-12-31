# The following problem is taken from Project Euler: 
# 
# ---Even Fibonacci Numbers---
# Each new term i nthe fibonacci sequence is generated by adding the previous two terms.
# By starting wit 1 and 2, the first 10 terms will be:
#   "1,2,3,5,8,13,21,34,55,89,..."
#
# By considering the terms in the Fibonacci sequence whos values DO NOT EXCEED FOUR MILLION (4000000), 
# find the sum of all the EVEN valued terms.

def main():
    fiboTerms = [1]
    evenTerms = []
    next = 2
    while next < 4000000:
        fiboTerms.append(next)
        next = fiboTerms[-2]+fiboTerms[-1]
    
    for term in fiboTerms:
        if term%2 == 0:
            evenTerms.append(term)
    print(sum(evenTerms))

if __name__ == "__main__":
    main()