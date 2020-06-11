import sys
from dataclasses import dataclass

@dataclass
class person:
    pref_position: int
    patience :int

def insertion_sort(array):
    l = len(array)                                  # define length of array
    for i in range(1,l):                                 # iterate through the array
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
    largest = len(array)                # find largest value in the array
    interval = 1      # define interval of each bucket

    for i in range(bucket_num):         # bucket_num is how many buckets wanted
        bucket.append([])               # make an empty bucket and place it in bucket array (bucket is a list of lists)
    for j in array:                     # iterate through elements of array
        if j.pref_position == largest:                # if element is the largest, add it to last bucket
            bucket[-1].append(j)
        else:                           # otherwise divide by the interval to decide which bucket to place it in
            index = j.pref_position-1     # index is the bucket id element will be placed in
            bucket[index].append(j)     # add the element to the appropriate bucket

    new_array = []

    for z in range(bucket_num):                 # iterate through buckets
        new_array.append(bucket[z][0])             # place it in to array

    return new_array                                # return the sorted array


def merge(array1, array2):
    array3 = []                                     # initialize empty array
    count = 0
    while len(array1) != 0 and len(array2) != 0:      # iterate through arrays until one is empty
        if array1[0].pref_position > array2[0].pref_position:   # if array1 first value greater than array2 first value
            array2[0].patience = array2[0].patience - len(array1)
            count = count + 1
            array3.append(array2[0])                # add the lower value to array3
            del array2[0]                           # remove from array2
        else:
            array3.append(array1[0])
            array1[0].patience = array1[0].patience - count   # else add array1 value to array3
            del array1[0]                           # remove value from array1
    while len(array1) != 0:                          # iterate through array1 until empty, and add values to array3
        array1[0].patience = array1[0].patience - count
        array3.append(array1[0])
        del array1[0]
    while len(array2)!= 0 :                          # iterate through array2 until empty, and add values to array3
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

def main():
    num_people = int(sys.stdin.readline())
    parade = []
    for p in range(num_people):
        person_list = sys.stdin.readline().split()
        person_list = [int(x) for x in person_list]
        x = person(person_list[0], person_list[1])
        parade.append(x)

    parade = merge_sort(parade)
    unhappy = 0
    for c in parade:
        if c.patience < 0:
            unhappy = unhappy +1
    print(unhappy)
    print(parade)
    return

if __name__ == '__main__':
    main()