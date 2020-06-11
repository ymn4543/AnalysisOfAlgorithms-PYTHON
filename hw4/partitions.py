"""
CSCI-261 Analysis of Algorithms hw-4 problem 2
Youssef Naguib
ymn4543@rit.edu
"""

import sys


"""
greedyEvans calculates the number of ways an array of integers
can be partitioned such that each partition has an even sum.
param array: list of integers
"""
def greedyEvens(array):
    sum = 0                 # total sum
    odds = 0                # number of odd numbers
    parts = 0
    ans = 0
    s = 0
    for i in range(0,len(array)):
        x = array[i]
        sum += x
        if x%2!= 0:
            odds +=1
        if odds%2 == 0:
            parts +=1
            ans = s + 1
            s= s + ans

    if sum%2 != 0:
        return 0

    return ans

"""
countOddPartitions calculates the number of ways an array of integers
can be partitioned such that each partition has an odd sum.
param array: list of integers
"""
def countOddPartitions(array):
    n = len(array)
    s = [0] * n
    odds = 0
    first_even = -1
    first_odd = -1
    for i in range(0,len(array)):
        if array[i]%2 !=0:
            odds+=1
            if first_odd == -1:     # find index of first odd
                first_odd = i
        else:
            if first_even<0:        # find index of first even
                first_even = i
    if odds ==0:
        return 0
    if odds == 1:
        return 1

    for i in range(0,first_odd+1):      # fill dynamic array with 1's until first odd
        s[i] = 1
    if first_odd == 0:
        s[0] = 1

    for x in range(first_odd+1,n):      # iterate through array
        element = array[x]
        if element%2==0:        # if element is even, it is same as previous value in dynamic array
            s[x] = s[x-1]

        else:                   # otherwise
            total = s[x-1]      # tack on every previous value in array, if sum is odd,
            sum = array[x]      # add it's index in dynamic array -1 to the total
            point = 1
            while point<=x:
                sum += array[x-point]
                if sum%2!=0:
                    total+=s[x-point-1]
                point+=1
            if array[0]%2!=0 and sum%2!=0:
                total +=1
            s[x] = total            # set dynamic array index to total

    return s[-1]



"""
main function reads in a list of integers, and prints out two values.
The first value is the number of ways an array of integers
can be partitioned such that each partition has an even sum.
The second value is the number of ways an array of integers
can be partitioned such that each partition has an odd sum.
"""
def main():
    n = int(sys.stdin.readline())           # length of array
    numbers = sys.stdin.readline().split()  # read in array
    numbers = [int(x) for x in numbers]
    x = greedyEvens(numbers)                # find even partitions and print
    print(x)
    z = countOddPartitions(numbers)         # find odd partitions and print
    print(z)
    return


if __name__ == '__main__':
    main()