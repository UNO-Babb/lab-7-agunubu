#Problem4.py
#Project Euler problem 4

from NumberTests import isPalindrome 

 
def main():
    maxPalindrome = 0
    factor1 = 0
    factor2 = 0

    for i in range(100, 1000):  
        for j in range(100, 1000):
            product = i * j
            if isPalindrome(product) and product > maxPalindrome:
                maxPalindrome = product
                factor1, factor2 = i, j
    print((maxPalindrome), "is the product of", factor1, "*", factor2)

if __name__ == '__main__':
  main()