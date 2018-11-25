import math

'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

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

'''
print(isPrime(7)) #True
print(isPrime(2)) #True
print(isPrime(17)) #True
print(isPrime(10)) #False
print(isPrime(14)) #False
'''

#Uses Pollard's rho algorthm to find largest prime factor of a number
def findLargestPF(num):

    #If the number is prime then just return the number
    if(isPrime(num)):
        return num

    a = 2
    b = 2
    counter = 0
    maxPrime = -1

    #While the function has not cycled or we have not yet begun finding the factor
    while(b != a or counter==0):
        counter+=1
        #f(a)
        a = ( (a * a) + 1 ) % num
        #print("a:",a)
        #Apply function twice f(f(b))
        b = int( ( math.pow(( (b * b) + 1 ) % num , 2) + 1 ) % num )
        #print("b:",b)
        factor = math.gcd( abs(b - a), num )

        #Check if non trivial and is a prime
        if( factor > 1 and isPrime(factor) ):
            if(factor > maxPrime):
                maxPrime = factor
                #print(maxPrime)
                #print("Counter:",counter)


        if(counter > int( math.sqrt(num) ) ):
            return maxPrime



    '''if( isPrime(num) ):
        return num

    max = -1
    for i in range(2, num):
        if(  (num % i == 0) and isPrime(i) ):
            max = i
    return max'''

print(findLargestPF(600851475143))
#print(isPrime(600851475143))
