import sys
from dataclasses import dataclass
"""
CSCI-261 Analysis of Algorithms hw-1 problem 4
Youssef Naguib
ymn4543@rit.edu
"""
# a dataclass representing a person
@dataclass
class person:
    id: int                     # person's id
    group : int                 # person's group (1 or 2)
    preference_list: list       # person's preference list
    match : int                 # current match's id
    last_asked : int            # index of last asked person in preference list


"""
Gale-Shapeley algorithm implementation. Finds a stable matching between
two groups. The algorithm will favor group1's preferences.
param group1: first group of people (profs)
param group2: second group of people (students)
"""
def gale_shapley(group1, group2):
    stack = []                      # stack will store all profs without a match
    for i in range(len(group1)):    # iterate through group1
        stack.append(group1[i])     # add each person to the stack
    while len(stack) != 0:          # iterate through the stack
        prof = stack[0]             # look at front of stack
        s = prof.preference_list[prof.last_asked]               # define who the prof will ask now (named s)
        if group2[s].match == None:                             # if s isn't matched
            prof.match = group2[s].id                           # match the professor and student
            group2[s].match = prof.id
            del stack[0]                                        # remove the prof from stack
        elif group2[s].preference_list.index(prof.id) < group2[s].preference_list.index(group2[s].match):
            stack.insert(0,group1[group2[s].match])         # if s is matched but prefers this prof, also match them
            del stack[1]                                    # remove prof from stack
            prof.match = group2[s].id
            group2[s].match = prof.id
        else:                                               # otherwise the prof will ask next person in their list
            prof.last_asked += 1
    return group1, group2                                   # return both groups



"""
main function creates people dataclasses based on input.
people are stored into two groups.
The Gale-Shapley algorithm is run on both groups twice.
The first run will favor the first group's preferences.
The second run will favor the second group's preferences.
If any of the matches from both runs are identical, the program prints out NO.
Otherwise the program prints out YES, indicating there is more than one stable matching
"""
def main():
    width = int(sys.stdin.readline())       # first number read in from input indicates how many people in one group
    group1 = []                             # initialize four arrays
    group2 = []
    group3 = []                             # a copy of group1
    group4 = []                             # a copy of group2
    for i in range(width):                  # read in input
        line = sys.stdin.readline()         # for each line,
        space = line.split(" ")
        pref_list = [int(i) for i in space]   # make the preference list
        x = person(i, 1, pref_list, None, 0)    # initialize the person twice
        y = person(i, 1, pref_list, None, 0)
        group1.append(x)                        # add to two arrays so we have two copies of same people
        group3.append(y)
    for i in range(width):                  # repeat process for second group
        line = sys.stdin.readline()
        space = line.split(" ")
        pref_list = [int(i) for i in space]
        x = person(i, 2, pref_list, None, 0)
        y = person(i, 2, pref_list, None, 0)
        group2.append(x)
        group4.append(y)

    tuple1 = []                     # initialize two arrays to store parings of each run
    tuple2 = []
    group1, group2 = gale_shapley(group1, group2)       # run the gale shapley algorithm favoring group1
    for i in group1:                                    # add pairings to tuple1 array
        tup = i.id,i.match
        tuple1.append(tup)
    group4,group3 = gale_shapley(group4, group3)       # run gale shapley algorithm favoring group2
    for v in group4:                                    # add pairings to tuple2 array
        tup = v.id,v.match
        tuple2.append(tup)

    for t in tuple1:                                # iterate through pairings in tuple1
        if t in tuple2:                             # if duplicate pairing found in tuple2, print NO and end program
            print("NO\n")
            return
    print("YES\n")                              # if no duplicate pairings found, print YES and end program
    return


if __name__ == '__main__':
    main()
