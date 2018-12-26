'''What is the sum of the digits of the number 2^1000?'''

def getSum():

    num = 2 ** 1000
    strNum = str(num)
    sum = 0
    for i in range(len(strNum)):
        #Convert the characters to ints and add them up
        sum += int(strNum[i])
    return sum

print(getSum())
