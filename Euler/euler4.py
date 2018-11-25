'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''


def largestPalindrome():

    product = 0
    largestPalindrome = 0

    #Looping through 3 digit numbers
    for i in range(100, 1000):
        a = i
        for j in range(100,1000):
            b = j
            #print("A:",a)
            #print("B:",b)
            product = a * b
            #If product is equivalent to reversed product
            if( str(product) == str(product)[::-1]):
                if( product > largestPalindrome):
                    largestPalindrome = product
                #print("A:",a)
                #print("B:",b)

    return largestPalindrome

print(largestPalindrome())
