"""
CSCI-261 Analysis of Algorithms hw-4 problem 3
Youssef Naguib
ymn4543@rit.edu
"""
import sys

"""
largest_sum_subsequence finds the largest sum in an increasing
subsequence in an array of integers. This algorithm builds off 
of the longest increasing subsequence problem.
"""
def largest_sum_subsequence(array):
    S = [[0, 0]] * len(array)               # create 2d dynamic array
    for k in range(0,len(array)):           # iterate through array
        S[k] = [1,array[k]]
        for j in range(0,k):            # find the largest sum that can start at this number
            if array[j] < array[k] and S[k][0]< S[j][0] +1 and array[k]+S[j][1]>S[k][1]:  # if item is larger, and sum is larger
                S[k][0] = S[j][0]+1                     # build up iterative solution
                S[k][1] = array[k] + S[j][1]
    el = []
    for e in S:
        el.append(e[1])
    return max(el)      # return the max sum found


"""
main function reads in an array of integers and outputs the correct
answer to the largest sum of increasing subsequence problem.
"""
def main():
    n = int(sys.stdin.readline())           # length of array
    numbers = sys.stdin.readline().split()  # read in array
    numbers = [int(x) for x in numbers]

    x = largest_sum_subsequence(numbers)    # find max sum
    print(x)                                # print max sum
    return


if __name__ == '__main__':
    main()
