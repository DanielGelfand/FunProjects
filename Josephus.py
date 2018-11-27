#Josephus Problem - Bit Magic
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
