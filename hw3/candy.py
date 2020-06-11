"""
Author: Youssef Naguib <ymn4543@rit.edu>
CSCI-261 hw-3 question 4 implementation
"""
import sys
import random

"""
select_rand() finds the k'th smallest element in an array.
param array: the sorted array of elements
param k: k represents position wanted. k==0 means the smallest element is wanted.
"""
def select_rand(array,k):
    random_number = random.randint(0, len(array)-1)     # generate a random int in range of array length
    x = array[random_number]                            # x is the element at that index in the array
    L = []                          # initialize bucket array for smaller, equal, and bigger elements
    E = []
    G = []
    for element in array:       # iterate through the array and store elements in appropriate bucket
        if element < x:
            L.append(element)
        if element == x:
            E.append(element)
        if element > x:
            G.append(element)
    if k < len(L):                  # if k is in the smaller array, recurse on L
        return select_rand(L,k)
    if k < (len(L) + len(E)):           # if k is in the equal bucket, return x
        return x
    else:                               # otherwise recurse on G
        new_k = k - len(L) - len(E)
        return select_rand(G,new_k)


"""
count_candies() calculates the maximum number of candies that can
be bought with a given allowance.
param allowance: how much money can be spent
param candy_prices: array of candy prices
"""
def count_candies(allowance, candy_prices):
    candies_bought = 0                                     # variable to keep track of types of candy bought
    while allowance > 0:                            # while user has money, find the next cheapest candy
        candy = select_rand(candy_prices,candies_bought)
        if allowance - candy < 0:                   # if user can't afford it, return candies_bought
            return candies_bought
        else:                                       # otherwise increase candies bought by one
            candies_bought = candies_bought + 1     # and subtract candy price from allowance
            allowance = allowance - candy
    return candies_bought



def main():
    allowance = int(sys.stdin.readline())               # this number represents how much money user can spend
    types_of_candy = int(sys.stdin.readline())          # this number represents the types of candy at store
    candy_prices = sys.stdin.readline().split()
    candy_prices = [int(x) for x in candy_prices]       # array of candy prices
    candies_bought = count_candies(allowance,candy_prices)  # find max number of candies that can be bought
    print(candies_bought)                                  # print counter variable and return
    return


if __name__ == '__main__':
    main()
