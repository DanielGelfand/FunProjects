# My solution requires num2words module
from num2words import num2words

#print(num2words(42))

def findSum():
    sum = 0
    for i in range(1,1001):

        # Convert num to word
        word = num2words(i)
        # Get rid of spaces and dashes
        word = word.replace("-", "").replace(" ","")
        #print(word)
        sum += len(word)
        
    return sum

print(findSum())
