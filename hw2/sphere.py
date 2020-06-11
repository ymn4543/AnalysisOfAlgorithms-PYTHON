"""
Author: Youssef Naguib <ymn4543@rit.edu>
CSCI-261 hw-2 question 3 implementation
"""

import sys
import math


"""
find_distance calculates the distance from the 3d point to the origin.
param x: x coordinate
param y: y coordinate
param z: z coordinate
"""
def find_distance(x, y, z):
    diff1 = (0 - x)*(0 - x)
    diff2 = (0 - y)*(0 - y)
    diff3 = (0 - z)*(0 - z)
    distance = math.sqrt(diff1+diff2+diff3)
    return distance

"""
insertion_sort implementation takes an array and orders its elements.
Param array: array to be sorted
"""
def insertion_sort(array):
    l = len(array)                                  # define length of array
    for i in range(1,l):                            # iterate through the array
        pointer = array[i]                          # define value at index (named pointer)
        left = i-1                                  # define value to left of index
        while left >= 0 and pointer < array[left]:  # while the left value is larger than pointer
            array[left+1] = array[left]             # move pointer left through the array
            left -= 1
        array[left+1] = pointer
    return array                                        # return sorted array


"""
bucket_sort implementation takes an array and orders its elements.
Param array: array to be sorted
"""
def bucket_sort(array):
    bucket = []                         # define empty list
    bucket_num = len(array)             # define number of buckets to be equal to length of array
    largest = max(array)                # find largest value in the array
    interval = largest/bucket_num       # define interval of each bucket

    for i in range(bucket_num):         # bucket_num is how many buckets wanted
        bucket.append([])               # make an empty bucket and place it in bucket array (bucket is a list of lists)
    for j in array:                     # iterate through elements of array
        if j == largest:                # if element is the largest, add it to last bucket
            bucket[-1].append(j)
        else:                           # otherwise divide by the interval to decide which bucket to place it in
            index = int(j/interval)     # index is the bucket id element will be placed in
            bucket[index].append(j)     # add the element to the appropriate bucket
    for x in range(bucket_num):         # go through every bucket
        bucket[x] = insertion_sort(bucket[x])   # sort the bucket using insertion sort

    n = 0                                       # the following concatenates all the buckets into one array
    for z in range(bucket_num):                 # iterate through buckets
        for y in range(len(bucket[z])):         # iterate through bucket's elements
            array[n] = bucket[z][y]             # place it in to array
            n = n + 1                           # increase index

    return array                                # return the sorted array



def main():
    numpoints = int(sys.stdin.readline())       # number of total points in input file
    distances = []                              # initialize an empty array for the distances
    for i in range(numpoints):                  # read every line in input and convert to int array of len 3
        line = sys.stdin.readline().split(' ')
        line = [int(c) for c in line]
        distance = find_distance(line[0], line[1], line[2])     # use the values in this array to calculate distance
        distances.append(distance)                              # of point from origin, and store that distance in the
                                                                # distances array
    distances = bucket_sort(distances)      # sort the array of distances using bucket sort O(n logn)
    for i in range(len(distances)-1):           # iterate through the sorted list O(n)
        if distances[i] == distances[i+1]:      # if the next item in the list is equal, print YES to indicate
            print("YES")                        # 2 points lie on same sphere surface
            return                              # end program
    print("NO")                                 # if no two points are equal, print NO and end program
    return


if __name__ == '__main__':
    main()