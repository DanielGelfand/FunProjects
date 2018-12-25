'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
'''

# Dynamic Programming

stored = {1: 1}
def collatzTerms(n):
    init = n
    counter = 1
    while n != 1:

        #If number was solved for before
        if n in stored.keys():
            #print("USING STORED VALUE")
            #stored[n] already includes the starting term so subtract 1
            stored[init] = (counter-1) + stored[n]
            return (counter-1) + stored[n];
        else:
            if(n % 2 == 0):
                n = n/2
                counter += 1
            else:
                n = 3 * n + 1
                counter += 1
    stored[init] = counter
    return counter

#print(collatzTerms(13)) #10
#print(collatzTerms(4)) #3

def largestChain():
    #Store largest amount of terms and associated number that produces that chain
    largest = 0
    result = 0

    for i in range(1,1000000):
        terms = collatzTerms(i)
        if(terms > largest):
            largest = terms
            result = i
    #print(stored)
    return result

print(largestChain())
