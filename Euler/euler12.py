'''What is the value of the first triangle number to have over
five hundred divisors?'''

import math

#Number of divisors for a number b
#Use the fact thaat divisors come in pairs
def numDivisors(n):

    result = 0

    #Divisors come in pairs
    for i in range(1, int(math.sqrt(n)) + 1) :

        if(n % i == 0):
            #if the divisors are the same
            if(n / i == i):
                result += 1;
            else:
                #Pair of divisors
                result += 2;
    return result

#print(numDivisors(6)) #4 since 1,2,3,6
#print(numDivisors(100)) #9 since 1 2 4 5 10 20 25 50 100

#Returns the nth triangular number
def triangularNum(n):
    return ( n * (n+1) ) /2

#print(triangularNum(5))
#print(triangularNum(6))
#print(triangularNum(7))
#print(triangularNum(200000000))

print(numDivisors(12375))

for i in range(100,10000000000):
    if( numDivisors( triangularNum(i) ) > 500 ):
        print( triangularNum(i) )
        break

#print(numDivisors(triangularNum(100000000)))
