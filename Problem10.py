#Problem10.py
#Project Euler problem 10

from NumberTests import isPrime
 
def main():
    sumPrime = 0 
    for s in range(2000000):
       if isPrime(s):
        sumPrime = sumPrime + s
    print(sumPrime)


if __name__ == '__main__':
  main()