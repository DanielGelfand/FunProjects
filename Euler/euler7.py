'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''

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


def nthprime(n):

    counter = 0
    for i in range(2, 1000000000):
        if( isPrime(i) ):
            counter +=1

        if(counter ==  n):
            return i

print(nthprime(10001))



'''
#Sieve of Eratosthenes to get primes
def sieve(n):
    multiples = []
    primes = []
    for i in range(2, n+1):
        if i not in multiples:
            primes.append(i)
            for j in range(i * i, n+1, i):
                multiples.append(j)
    #print(primes)
    return primes

#Prime counting function - counts number of primes less than or equal to n
def pi(n):
    return len(sieve(n))
'''

#print(pi(100000))
