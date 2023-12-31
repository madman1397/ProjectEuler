# The following problem is taken from Project Euler: 
#
# ---Largest Palindrome Product---
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers

def checkPalindromes(fProd):
    firstHalf = fProd[:len(fProd)//2]
    secondHalf = "".join(reversed(fProd[len(fProd)//2:]))
    if firstHalf == secondHalf:
        return True
    else: return False
def main():
    top = 0
    x,y = 1,1
    while x < 1000:
        while y < 1000:
            prod = x*y
            print(f"{x}*{y}={prod}")
            if checkPalindromes(str(prod)) and prod > top:
                top = prod
            y+=1
        y=1
        x+=1
    print(top)

if __name__ == "__main__":
    main()