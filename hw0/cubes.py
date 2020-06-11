"""
CSCI-261 Analysis of Algorithms hw-0 problem 1
Youssef Naguib
ymn4543@rit.edu
"""
import sys  # to read from standard input


"""
This program reads in one number from standard input and prints all perfect 
cubes between 0 and that number to standard output. Program then terminates.
"""
def main():
    var1 = int(sys.stdin.readline())    # var1 is the integer read from input
    count = 0                           # count is a counter variable
    while(count*count*count) <= var1:
        print(count*count*count)
        count = count + 1
    quit()


if __name__ == '__main__':
    main()
