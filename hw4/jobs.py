"""
CSCI-261 Analysis of Algorithms hw-4 problem 1
Youssef Naguib
ymn4543@rit.edu
"""
import sys

"""
merge is a helper function for merge_sort. It takes two ordered
arrays and combines them into one ordered array.
Param array1: first array
Param array2: second array
"""
def merge(array1, array2):
    array3 = []                                     # initialize empty array
    while len(array1)!= 0 and len(array2)!= 0:      # iterate through arrays until one is empty
        if array1[0][1] > array2[0][1]:                   # if array1 first value greater than array2 first value
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
This version sorts jobs by end time.
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
choose_jobs takes a list of jobs from 2 employers and returns the max
number of compatible jobs that can be chosen, given that each job must
alternate between employers.
param array: list of jobs
param employer_pref: either 0 or 1 (the employer that will provide the first job)
"""
def choose_jobs(array, employer_pref):
    jobs_selected = 0
    x = employer_pref
    job_end = 0
    for job in array:
        if job[2] == x and job[0]>=job_end:
            jobs_selected +=1
            job_end = job[1]
            if x == 0:
                x = 1
            elif x == 1:
                x = 0
    return jobs_selected

"""
in this problem jobs are represented as arrays with three elements, the third being which
employer they belong to (0 for employer 1, 1 for employer 2). The first element is the start
time and the second element is the end time. Main function reads in input and solves the
optimal scheduling problem.
"""
def main():
    jobs = int(sys.stdin.readline()) # number of total jobs
    employers = []                   # list of jobs
    for j in range(0,jobs):
        line = sys.stdin.readline().split()
        line = [int(x) for x in line]
        employers.append(line)       # add each job to list


    employers = merge_sort(employers)    # sort jobs by earliest end times
    run_1 = choose_jobs(employers,0)     # find most jobs possible if starting with job from employer 1
    run_2 = choose_jobs(employers,1)     # find most jobs possible if starting with job from employer 2
    m = max(run_1,run_2)                   # find the max of these two values
    print(m)
    return


if __name__ == '__main__':
    main()
