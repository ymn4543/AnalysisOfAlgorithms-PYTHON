"""
CSCI-261 Analysis of Algorithms hw-1 problem 3
Youssef Naguib
ymn4543@rit.edu
"""
import sys      # to read from standard input

"""
This function checks to see if more than half of the total snow falls within a
three day period. 
Param days: number of days of snowfall
Param totals: list containing cumulative snowfall data per day
"""
def check_snow(days,totals):
    snow_sum = (totals[days-1])/2  # the total cumulative snowfall
    pointer = 0                    # represents the first day of 3 day interval
    while pointer <= (days-4):      # while the three day interval is in bounds
        day1 = totals[pointer]         # snowfall on first of three days
        day3 = totals[pointer+3]       # snowfall on last of three days
        if day3 - day1 > snow_sum:  # if more than half of snow fell in this interval, print YES
            print("YES")
            return
        else:
            pointer += 1            # otherwise increase the index representing day1
                # new day3 value
    print("NO")                         # if no intervals had more than half of total snowfall, print NO
    return


def main():
    days = int(sys.stdin.readline())        # read in total number of days in range
    totals = sys.stdin.readline().split()   # split values into string array
    totals = [int(i) for i in totals]       # convert string array to int array
    check_snow(days, totals)                # call function to check if more than half of all snow fell within 3 days


if __name__ == '__main__':
    main()
