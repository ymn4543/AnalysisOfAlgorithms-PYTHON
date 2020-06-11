"""
CSCI-261 Analysis of Algorithms hw-1 problem 5
Youssef Naguib
ymn4543@rit.edu
"""
import random
import time

"""
merge is a helper function for merge_sort. It takes two ordered
arrays and combines them into one ordered array.
Param array1: first array
Param array2: second array
"""
def merge(array1, array2):
    array3 = []                                     # initialize empty array
    while len(array1)!= 0 and len(array2)!= 0:      # iterate through arrays until one is empty
        if array1[0] > array2[0]:                   # if array1 first value greater than array2 first value
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
merge_sort implementation takes an array and orders its elements.
Param array: array to be sorted
"""
def merge_sort(array):
    if len(array) == 1:                 # if the array has a single element, return the array
        return array
    array1 = array[:len(array)//2]      # array1 is first half of array
    array2 = array[len(array)//2:]      # array2 is other half of array
    array1 = merge_sort(array1)         # recursive call on array1
    array2 = merge_sort(array2)         # recursive call on array2
    return merge(array1, array2)        # merge array1 and array2, and return


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

"""
random_floats returns an array of random numbers in the range (0,1]
Param array: size of array to be returned
"""
def random_floats(size):
    return [round(random.uniform(0, .999),3) for x in range(size)]  # return an array of random floats

"""
random_floats returns an array of random numbers in the range (0,1]
using a guassian distribution with mew = .5 and sigma = 1/10000
Param array: size of array to be returned
"""
def random_guass(size):
    return [round(random.gauss(.5,(1/10000)),3) for x in range(size)]   # return a array of random floats

"""
main function runs tests on all three sorting algorithms.
tests are run on both uniform and guassian 
arrays of size 100, 1000, 10000, and 100000, and runtimes are printed
"""
def main():
    # insertion sort tests

    insertion_array_100 = random_floats(100)                # initialize uniform array of size 100
    insertion_array_1000 = random_floats(1000)              # initialize uniform array of size 1000
    insertion_array_10000 = random_floats(10000)            # initialize uniform array of size 10000
    insertion_array_100000 = random_floats(100000)          # initialize uniform array of size 100000
    gauss_insertion_array_100 = random_guass(100)           # initialize gaussian dist. array of size 100
    gauss_insertion_array_1000 = random_guass(1000)         # initialize gaussian dist. array of size 1000
    gauss_insertion_array_10000 = random_guass(10000)       # initialize gaussian dist. array of size 10000
    gauss_insertion_array_100000 = random_guass(100000)     # initialize gaussian dist. array of size 100000

    # run insertion sort tests on all arrays, and print runtime

    then = time.time()
    insertion_sort(insertion_array_100)
    now = time.time()
    print("insertion sort on uniform array of size 100 took", now - then, "seconds")
    then = time.time()
    insertion_sort(insertion_array_1000)
    now = time.time()
    print("insertion sort on uniform array of size 1000 took", now - then, "seconds")
    then = time.time()
    insertion_sort(insertion_array_10000)
    now = time.time()
    print("insertion sort on uniform array of size 10000 took", now - then, "seconds")
    then = time.time()
    # insertion_sort(insertion_array_100000)
    now = time.time()
    print("insertion sort on uniform array of size 100000 took more than 3 minutes ")
    then = time.time()
    insertion_sort(gauss_insertion_array_100)
    now = time.time()
    print("insertion sort on guassian array of size 100 took", now - then, "seconds")
    then = time.time()
    insertion_sort(gauss_insertion_array_1000)
    now = time.time()
    print("insertion sort on guassian array of size 1000 took", now - then, "seconds")
    then = time.time()
    insertion_sort(gauss_insertion_array_10000)
    now = time.time()
    print("insertion sort on guassian array of size 10000 took", now - then, "seconds")
    then = time.time()
    insertion_sort(gauss_insertion_array_100000)
    now = time.time()
    print("insertion sort on guassian array of size 100000 took", now - then, "seconds")

    # merge sort tests

    merge_array_100 = random_floats(100)                         # initialize uniform array of size 100
    merge_array_1000 = random_floats(1000)                       # initialize uniform array of size 1000
    merge_array_10000 = random_floats(10000)                     # initialize uniform array of size 10000
    merge_array_100000 = random_floats(100000)                   # initialize uniform array of size 100000
    gauss_merge_array_100 = random_guass(100)                    # initialize gaussian dist. array of size 100
    gauss_merge_array_1000 = random_guass(1000)                  # initialize gaussian dist. array of size 1000
    gauss_merge_array_10000 = random_guass(10000)                # initialize gaussian dist. array of size 10000
    gauss_merge_array_100000 = random_guass(100000)              # initialize gaussian dist. array of size 100000

    # run merge sort tests on all arrays, and print runtime

    then = time.time()
    merge_sort(merge_array_100)
    now = time.time()
    print("merge sort on uniform array of size 100 took ", now-then, "seconds")
    then = time.time()
    merge_sort(merge_array_1000)
    now = time.time()
    print("merge sort on uniform array of size 1000 took ", now-then, "seconds")
    then = time.time()
    merge_sort(merge_array_10000)
    now = time.time()
    print("merge sort on uniform array of size 10000 took ", now-then, "seconds")
    then = time.time()
    merge_sort(merge_array_100000)
    now = time.time()
    print("merge sort on uniform array of size 100000 took", now-then, "seconds")
    then = time.time()
    merge_sort(gauss_merge_array_100)
    now = time.time()
    print("merge sort on guass array of size 100 took ", now-then, "seconds")
    then = time.time()
    merge_sort(gauss_merge_array_1000)
    now = time.time()
    print("merge sort on guass array of size 1000 took ", now-then, "seconds")
    then = time.time()
    merge_sort(gauss_merge_array_10000)
    now = time.time()
    print("merge sort on guass array of size 10000 took ", now-then, "seconds")
    then = time.time()
    merge_sort(gauss_merge_array_100000)
    now = time.time()
    print("merge sort on guass array of size 100000 took ", now-then, "seconds")

    # bucket sort tests

    bucket_array_100 = random_floats(100)                    # initialize uniform array of size 100
    bucket_array_1000 = random_floats(1000)                  # initialize uniform array of size 1000
    bucket_array_10000 = random_floats(10000)                # initialize uniform array of size 10000
    bucket_array_100000 = random_floats(100000)              # initialize uniform array of size 100000
    bucket_guass_array_100 = random_guass(100)               # initialize gaussian dist. array of size 100
    bucket_guass_array_1000 = random_guass(1000)             # initialize gaussian dist. array of size 1000
    bucket_guass_array_10000 = random_guass(10000)           # initialize gaussian dist. array of size 10000
    bucket_guass_array_100000 = random_guass(100000)         # initialize gaussian dist. array of size 100000

    # run bucket sort tests on all arrays, and print runtime

    then = time.time()
    bucket_sort(bucket_array_100)
    now = time.time()
    print("bucket sort on uniform array of size 100 took ", now-then, "seconds")
    then = time.time()
    bucket_sort(bucket_array_1000)
    now = time.time()
    print("bucket sort on uniform array of size 1000 took ", now-then, "seconds")
    then = time.time()
    bucket_sort(bucket_array_10000)
    now = time.time()
    print("bucket sort on uniform array of size 10000 took ", now-then, "seconds")
    then = time.time()
    bucket_sort(bucket_array_100000)
    now = time.time()
    print("bucket sort on uniform array of size 100000 took ", now-then, "seconds")
    then = time.time()
    bucket_sort(bucket_guass_array_100)
    now = time.time()
    print("bucket sort on guass array of size 100 took", now - then, "seconds")
    then = time.time()
    bucket_sort(bucket_guass_array_1000)
    now = time.time()
    print("bucket sort on guass array of size 1000 took", now - then, "seconds")
    then = time.time()
    bucket_sort(bucket_guass_array_10000)
    now = time.time()
    print("bucket sort on guass array of size 10000 took", now - then, "seconds")
    then = time.time()
    bucket_sort(bucket_guass_array_100000)
    now = time.time()
    print("bucket sort on guass array of size 100000 took", now - then, "seconds")


if __name__ == '__main__':
    main()