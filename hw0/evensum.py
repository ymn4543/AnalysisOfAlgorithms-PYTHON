"""
CSCI-261 Analysis of Algorithms hw-0 problem 2
Youssef Naguib
ymn4543@rit.edu
"""

import sys  # to read from standard input

"""
This program returns the sum of all the even numbers given by standard
input. The first number given represents how many following numbers will
be entered, and is not included in the sum. A builtin python list is used to 
store all the entered numbers, then a while loop iterates through all the
indices between 0 and the first entered number. Index access is an O(1) time
operation, so this algorithm is very efficient and quick. 
"""
def main():
    number = int(sys.stdin.readline())  # first number read from input representing quantity of entries
    numlist = []     # empty list of integers (builtin python list)
    count = 0       # counter variable
    total = 0       # sum variable
    while count < number:
        numlist.insert(count, int(sys.stdin.readline()))
        count = count + 1
    count = 0
    while count < len(numlist):
        if numlist[count] % 2 == 0:
            total += numlist[count]
        else:
            pass
        count += 1
    print(total)        # print the sum before terminating
    quit()


if __name__ == '__main__':
    main()
