#Problem4.py
#Project Euler problem 4

from NumberTests import isPalindrome 

 
def main():
    maxPalindrome = 0

    for i in range(100, 1000):  
        for j in range(100, 1000):
            product = i * j
            if isPalindrome(product) and product > maxPalindrome:
                maxPalindrome = product
    print(maxPalindrome)

if __name__ == '__main__':
  main()