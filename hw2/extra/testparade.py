import sys
from dataclasses import dataclass

@dataclass
class person:
    pref_position: int
    patience :int




def merge(array1, array2):
    array3 = []                                     # initialize empty array
    count = 0
    while len(array1) != 0 and len(array2) != 0:      # iterate through arrays until one is empty
        if array1[0][0] > array2[0][0]:   # if array1 first value greater than array2 first value
            array2[0][1] = array2[0][1] - len(array1)
            count = count + 1
            array3.append(array2[0])                # add the lower value to array3
            del array2[0]                           # remove from array2
        else:
            array3.append(array1[0])
            array1[0][1] = array1[0][1] - count   # else add array1 value to array3
            del array1[0]                           # remove value from array1
    while len(array1) != 0:                          # iterate through array1 until empty, and add values to array3
        array1[0][1] = array1[0][1] - count
        array3.append(array1[0])
        del array1[0]
    while len(array2) != 0 :                          # iterate through array2 until empty, and add values to array3
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
        x = [person_list[0], person_list[1]]
        parade.append(x)

    parade = merge_sort(parade)
    unhappy = 0
    for c in parade:
        if c[1] < 0:
            unhappy = unhappy + 1
    print(unhappy)
    return

if __name__ == '__main__':
    main()