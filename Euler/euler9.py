'''There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.'''

import math

#Finds the value of c in pythagorean triplet
def findC(a,b):
    return math.pow( math.pow(a,2) + math.pow(b,2) , .5)

#print(findC(3,4));

def findProd():
    c = 0
    for a in range(1, 10000):
        for b in range(1,10000):
            c = findC(a,b)
            if(a + b + c == 1000):
                #print(a,b,c)
                return a * b * c
print(findProd())
