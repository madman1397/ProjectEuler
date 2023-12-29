# The following problem is taken from Project Euler.
# Challenge 1 prompt:
# If we list all the natural numbers (positive integers) that are multiples of 3 or 5,
# we get 3,5,6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000

def main():
    multList = []
    for i in range(1,1000):
        if i%3 == 0 or i%5 == 0:
            multList.append(i)

    print(f"the sum of all multiples of 3 and 5 below 1000 is {sum(multList)}")

if __name__ == '__main__':
    main()