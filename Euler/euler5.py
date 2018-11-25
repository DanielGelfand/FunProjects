'''2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder. What is the smallest positive number
that is evenly divisible by all of the numbers from 1 to 20?
'''

def smallestDividend():

    #Increment 2520 to maintain property of divisibiity by first 10 numbers
    for i in range(2520, 300000000,2520):

        valid = True

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
