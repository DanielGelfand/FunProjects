#Josephus Problem - Bit Magic
#Given n people in a circle numbered 1 to n, get the winning number using binary shortcut
#Assume every second person is killed
def getWinner(n):
    return int( str(bin(n)[3:]) + str(bin(n)[2]) , 2)

#Josephus Problem using Recursive solution
#Every kth person is killed
def getWinnerRec(n,k):

    if(n==1):
        return 1

    return (getWinnerRec(n-1,k) + k-1) % n+1

#print(  str(bin(4)[3:]) + str(bin(4)[2])  )


print(getWinner(1))
print(getWinner(32))
print(getWinner(13))
print(getWinner(3))
print(getWinner(16))
print(getWinner(15))
print(getWinner(14))

print()

print(getWinnerRec(1,2))
print(getWinnerRec(32,2))
print(getWinnerRec(13,2))
print(getWinnerRec(3,2))
print(getWinnerRec(16,2))
print(getWinnerRec(15,2))
print(getWinnerRec(14,2))
