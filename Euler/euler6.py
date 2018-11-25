'''
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''

import math

def difference(nums):

    #Formula for sum of artihmetic series
    squareOfSum = math.pow(nums *  ( (1 + nums) / 2 ) , 2)
    print(squareOfSum)
    sumOfSquares = ( nums * (nums+1) * (2 * nums + 1) ) / 6
    print(sumOfSquares)
    return squareOfSum - sumOfSquares

#print(difference(10))
print(difference(100))
