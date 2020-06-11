"""
Author: Youssef Naguib <ymn4543@rit.edu>
CSCI-261 hw-3 question 3 implementation
"""
import sys
import math

"""
n3_solution() is an O(n^3) solution to the problem. It calculates the number of right trinagles
given n points using dot products of vectors. Given angle ABC, the angle between these two points
is 90 if the dot product of the vectors AB and BC are 0.
param array: array of 2d points in Q1
"""
def n3_solution(array):
    num_right_triangles = 0
    for a in range(0,len(array)-2):
        for b in range(a+1,len(array)-1):
            for c in range(b+1,len(array)):
                ab = [array[b][0]-array[a][0], array[b][1]-array[a][1]]
                bc = [array[c][0]-array[b][0], array[c][1]-array[b][1]]
                ac = [array[c][0]-array[a][0], array[c][1]-array[a][1]]
                ab_dot_bc = (ab[0]*bc[0]) + (ab[1]*bc[1])
                ab_dot_ac = (ab[0]*ac[0]) + (ab[1]*ac[1])
                bc_dot_ac = (bc[0]*ac[0]) + (bc[1]*ac[1])
                if ab_dot_ac == 0 or ab_dot_bc == 0 or bc_dot_ac == 0:
                    num_right_triangles = num_right_triangles +1
    return num_right_triangles


"""
merge2() is a modified merge that aids merge_sort2() in sorting
two arrays of fractions.
param array1: first array 
param array2: second array
"""
def merge2(array1, array2):
    array3 = []                                     # initialize empty array
    while len(array1)!= 0 and len(array2)!= 0:      # iterate through arrays until one is empty
        if array1[0][0]/array1[0][1] > array2[0][0] / array2[0][1]:                   # if array1 first value greater than array2 first value
            array3.append(array2[0])                # add the lower value to array3
            del array2[0]                           # remove from array2
        else:
            array3.append(array1[0])                # else add array1 value to array3
            del array1[0]                           # remove value from array1
    while len(array1)!=0 :                          # iterate through array1 until empty, and add values to array3
        array3.append(array1[0])
        del array1[0]
    while len(array2)!=0 :                          # iterate through array2 until empty, and add values to array3
        array3.append(array2[0])
        del array2[0]

    return array3                                   # return array3, the combined array

"""
merge_sort2() is a modified merge_sort that sorts non-decimal fractions.
A fraction is represented as an array with two elements. The numerator is the first element
and the denominator is the second.
Param array: array to be sorted
"""
def merge_sort2(array):
    if len(array) == 1:                 # if the array has a single element, return the array
        return array
    array1 = array[:len(array)//2]      # array1 is first half of array
    array2 = array[len(array)//2:]      # array2 is other half of array
    array1 = merge_sort2(array1)         # recursive call on array1
    array2 = merge_sort2(array2)         # recursive call on array2
    return merge2(array1, array2)        # merge array1 and array2, and return

"""
binary_search2() is a modified binary search that searched through an
array of fractions to find the element wanted. If element isn't found,
the method returns -1
param array: array to search
param element: element in array wanted
"""
def binary_search2(array, element):
    low = 0
    high = len(array)-1
    while low <= high:
        middle = (low + high)//2
        if array[middle][0]/ array[middle][1] == element[0]/element[1]:
            return middle
        elif array[middle][0] / array[middle][1] > element[0]/element[1]:
            high = middle - 1
        else:
            low = middle + 1
    return -1


"""
num_right_triangles is an O(n^2logn) solution to finding the number of right angles
given n 2d points.
param array: an array of 2d points in Q1.
"""
def num_right_triangles(array):
    count = 0                           # variable stores number of right triangles
    for z in range(0, len(array)):      # iterate through each point
        main_point = array[z]
        slope_list = []
        rise_list = []
        vertical_lines = 0              # variable for undefined slopes
        for f in range(0,len(array)):       # iterate through each point
            y = array[f]
            if y!= main_point:              # if not same point
                if y[0] == main_point[0]:                   # if slope undefined, increase vertical lines variable
                    vertical_lines = vertical_lines + 1
                else:                               # if slope defined, store as a rise over run fraction in array
                    rise = y[1] - main_point[1]
                    run = y[0] - main_point[0]
                    rise_over_run = [rise,run]
                    rise_list.append(rise_over_run)

        rise_list = merge_sort2(rise_list)          # sort the slopes using merge sort
        minicount = 0                               # count of right triangles possible for this point
        while len(rise_list) > 0:                       # while slope array isn't empty
            slope = rise_list[0][0] / rise_list[0][1]
            if slope == 0 or slope == -0:               # if slope is 0, increase count by # of vertical lines
                minicount = minicount + vertical_lines
            else:                                                       # otherwise calculate inverse slope fraction
                neg_slope = [-1.0 * rise_list[0][1], rise_list[0][0]]
                index = binary_search2(rise_list, neg_slope)            # search for inverse fraction in array of slopes
                if index != -1:
                    minicount = minicount + 1         # increase count by number of repetitions of the inverse slope
                    i = 1                             # in the slope array, check neighbouring indices
                    while (index-i) >= 0:
                        if rise_list[index-i][0]/rise_list[index-i][1] == neg_slope[0]/neg_slope[1]:
                            minicount = minicount + 1
                            i = i + 1
                        else:
                            break
                    j = 1
                    while (index+j) < len(rise_list):
                        if rise_list[index+j][0]/rise_list[index+j][1] == neg_slope[0]/neg_slope[1]:
                            minicount = minicount + 1
                            j = j + 1
                        else:
                            break

            del rise_list[0]          # remove the first slope in the slope array so no duplicate angles are counted
        count = count + minicount       # add the mini count to the total count
    return count                    # return the total number of right triangles


"""
main function takes in input from user and calls appropriate
functions to calculate correct output (number of right triangles)
"""
def main():
    num_points = int(sys.stdin.readline())      # variable represents the total number of points
    points = []
    for i in range(num_points):                  # read every line in input and add to points array
        line = sys.stdin.readline().split(' ')
        line = [int(c) for c in line]
        points.append(line)
    x = num_right_triangles(points)   # calculate number of right triangles possible with any combination of 3 points
    print(x)                          # print result to user
    return


if __name__ == '__main__':
    main()
