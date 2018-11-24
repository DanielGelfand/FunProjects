from timeit import default_timer as timer

'''
Wallis Product

(2/1) * (2/3) * (4/3) * (4/5) * (6/5) * (6/7) ...
Should converge to pi/2 ~ 1.57
'''
def simulateWallis():
    #start = timer()
    #Initial Numerator and denominator
    num = 2
    den = 1
    counter = 1
    product = 1
    #Simulate (n) times
    for i in range(100000):

        '''if(counter == 500000):
            print("**********HALFWAY************")
            print("PRODUCT: ",product)
            print("*****************************")
        '''

        print("Counter: ",counter)
        print(str(num) + "/" + str(den))

        product = product * (num / den)
        print(product)
        if(counter > 0 and (counter%2==0) ):
            num += 2
        if( (counter-1)%2 == 0 ):
            den += 2

        counter+=1
    #end = timer()
    #print("Time elapsed: ", (end-start))
    return product

def simulateWallisNoPrint():
    #start = timer()
    #Initial Numerator and denominator
    num = 2
    den = 1
    counter = 1
    product = 1
    #Simulate (n) times
    for i in range(100000):

        '''if(counter == 500000):
            print("**********HALFWAY************")
            print("PRODUCT: ",product)
            print("*****************************")
        '''

        #print("Counter: ",counter)
        #print(str(num) + "/" + str(den))

        product = product * (num / den)
        #print(product)
        if(counter > 0 and (counter%2==0) ):
            num += 2
        if( (counter-1)%2 == 0 ):
            den += 2

        counter+=1
    #end = timer()
    #print("Time elapsed: ", (end-start))
    return product


def avgTime(numRuns):

    avg = 0
    #Run 5 times
    for i in range(numRuns):
        #Start timer and end it when simulation is complete
        start = timer()
        simulateWallisNoPrint()
        end = timer()
        avg += (end - start)

    avg = avg / numRuns

    return avg

print(avgTime(5))

'''
*******DATA*******
Result - 1.570796 after 1*10^6 runs

With 100,000 runs result was 1.570788

Time elapsed based on average of 5 runs
Time elapsed: 42.137 seconds with print statements
Time elapsed: 0.0265 seconds without print statements

There is an astonishing difference between the two.
'''
