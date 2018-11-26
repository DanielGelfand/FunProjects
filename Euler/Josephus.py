import math

#Simulate the Josephus problem
def simulate(n):

    circle = []

    if(circle.count(True) == 1):
        print("Simulation complete")
        print("The last standing survivor is number",getWinner(n))

    print("There are", n, "people in a circle")



    #Generate a circle of people where true represents alive and False represents dead
    #Since the lists starts at index 0, pretend index 0 is equivalent to a person numbered 1 in the circle
    for i in range(0,n):
        if(i%2==0):
            circle.append(True)
        else:
            circle.append(False)
        #print(circle[i])

    #Start killing off the odds(evens in this case)

    #If the number of people is even then start killing off from index 0
    if(n % 2 == 0):
        for i in range(2,n,2):
            circle[i] = False

    #for i in range(0,n):
        #print(circle[i])


#Given n people in a circle numbered 1 to n, get the winning number using binary shortcut
def getWinner(n):
    return int( str(bin(n)[3:]) + str(bin(n)[2]) , 2)

#print(  str(bin(4)[3:]) + str(bin(4)[2])  )

'''
print(getWinner(1))
print(getWinner(32))
print(getWinner(13))
print(getWinner(3))
'''
simulate(4)
