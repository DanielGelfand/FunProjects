'''2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder. What is the smallest positive number
that is evenly divisible by all of the numbers from 1 to 20?
'''

def smallestDividend():

    for i in range(2525, 300000000):

        valid = True

        #Preliminary factors tests
        if(i%2 != 0 or i%5!=0 or i%4!=0 or i%3!=0):
            continue
        #print(i)
        for j in range(11, 21):

            #print("I:",i)
            #print("J:",j)
            #If there is a remainer than i is not valid
            if( i%j != 0 ):
                valid = False
                break
            #print(valid)
        if(valid):
            return i

    return -1
    
print(smallestDividend())
