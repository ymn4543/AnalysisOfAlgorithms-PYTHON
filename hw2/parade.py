"""
Author: Youssef Naguib <ymn4543@rit.edu>
CSCI-261 hw-2 question 5 implementation
"""
import sys

"""
inversion_sort is a sorting algorithm that uses a modification of merge sort.
the function takes in an array and uses merge sort to sort it, meanwhile 
keeping track of the inversions that occur. The function returns how many 
participants have lost their patience. Patience is lost if it is below 0.
param array: the array ot be sorted
"""
def inversion_sort(array):
    unhappy = 0                # a count of how many participants have lost their patience
    if len(array) > 1:         # if array has more than one element
        middle = len(array) // 2      # split it into two half arrays
        left = array[:middle]
        right = array[middle:]
        inversion_sort(left)             # merge sort step where both halves are recursively called
        inversion_sort(right)

        i = 0                            # counter for left list index
        j = 0                            # counter for right list index
        k = 0                            # counter for original list index
        count = 0                        # count of how many inversions occur
        while i < len(left) and j < len(right):   # while both of the lists are't empty
            if left[i][0] < right[j][0]:          # if left list value lower than right list value
                array[k] = left[i]                # add the left list value to the original list
                array[k][1] = array[k][1] - count   # take away the number of inversions from its patience
                if array[k][1]<0:                   # if the patience is below 0
                    unhappy = unhappy+1             # increase unhappiness counter by 1
                i += 1                              # increase index of left list counter
            else:                                   # otherwise if right list value is lower
                right[j][1] = right[j][1] - (len(left) - i)     # take away number of swaps it will do from its patience
                if right[j][1] < 0:                 # if the patience is below 0
                    unhappy = unhappy+1             # increase unhappiness counter by 1
                count = count +1                    # increase the count of inversions by one
                array[k] = right[j]                 # add it to the original list
                j += 1                              # increase the index of right list counter
            k += 1                                  # increase index of original list counter

        while i < len(left):                        # while left list hasn't been traversed
            array[k] = left[i]                      # add value to original list
            array[k][1] = array[k][1] - count       # take away correct number of inversions from its patience
            if array[k][1] < 0:                     # if the patience is below 0
                unhappy = unhappy+1                 # increase unhappiness counter by 1
            i += 1                                  # increase index of left list
            k += 1                                  # increase index of original list
        while j < len(right):                       # while right list hasn't been traversed
            array[k]=right[j]                       # add values to original list
            if array[k][1] < 0:                     # if the patience is below 0
                unhappy = unhappy+1                 # increase unhappiness counter by 1
            j += 1                                  # increase right list counter index
            k += 1                                  # increase original list counter index
    return unhappy                                  # return number of unhappy participants


def main():
    num_people = int(sys.stdin.readline())          # number of people in parade line (first line in input)
    parade = []                                     # empty array that will represent the line
    for p in range(num_people):                     # iterate through input and store people as int arrays
        person_list = sys.stdin.readline().split()
        person_list = [int(x) for x in person_list]         # the first element represents their patience
        x = person_list                                     # the second element represents their correct position
        parade.append(x)                                    # add them to into the line
    unhappy = inversion_sort(parade)        # sort them using a modified merge sort, store number of unhappy participants
    print(unhappy)                         # print out that number and end program
    return

if __name__ == '__main__':
    main()