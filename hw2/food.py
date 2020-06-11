"""
Author: Youssef Naguib <ymn4543@rit.edu>
CSCI-261 hw-2 question 4 implementation
"""

import sys
import heapq



"""
no_food_wasted checks if a heap has any values below 0, indicating foods that 
have expired.
param heap: heap array storing shelf lives
"""
def no_food_wasted(heap):
    count = 0                   # count of how many days have passed
    for i in range(len(heap)):  # iterate through each item in array
        heap[0] = heap[0] - count   # take away shelf life based on days passed
        if heap[0] <= 1:            # if value below zero, print NO and return
            print("NO")
            return
        heapq.heappop(heap)         # remove that item from the heap
        count = count +1            # add a day to count
    print("YES")                    # print YES
    return



def main():
    food_items = int(sys.stdin.readline())      # number of total food items (first line in input)
    heap = []                                   # initialize empty array
    heapq.heapify(heap)                         # convert array to min heap
    day = 0                                     # day counter, set to 0
    for item in range(food_items):              # iterate through lines of input
        food = sys.stdin.readline().split()
        food = [int(x) for x in food]           # convert lines to int array, where first entry is the day it arrived
                                                # and second entry is the shelf life in days
        foodday = food[0]                       # keep track of day entry day
        if foodday == day:                      # if equal to day
            heapq.heappush(heap,food[1])            # add the shelf life to the heap
        else:                                   # otherwise
            diff = foodday - day                    # calculate the days between current day and entry day of item
            for d in range(diff):                   # for every day in that range
                if len(heap) == 0:                  # if there are no other items in heap, fast forward to that day
                    day = foodday
                    break
                root = heap[0]                      # root is the highest priority item
                if root <= 0:                       # if it is expired
                    print("NO")                     # return no
                    return
                for i in range(len(heap)):          # take away 1 from each food item's shelf life in heap
                    heap[i] = heap[i] - 1
                day = day + 1                       # move to next day
                heapq.heappop(heap)                 # remove the highest priority item to cook for that day
            heapq.heappush(heap,food[1])        # add the new item to the heap

    no_food_wasted(heap)            # check for any expired items in heap
    return

if __name__ == '__main__':
    main()