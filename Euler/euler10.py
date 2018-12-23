'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.'''

import math

#Trial dvision method to check if number is prime
def isPrime(num):

    for i in range( 2, int(math.sqrt(num)) + 1 ):

        #No need to check number if it is even and greater than 2
        if( i > 2 and (i%2==0) ):
            continue
        else:
            if(num % i  == 0):
                return False
    return True


def sumPrimes(bound):
    sum = 0
    for i in range(2, bound):
        if(isPrime(i)):
            #print("Prime",i)
            sum += i
    return sum
print(sumPrimes(2000000))
