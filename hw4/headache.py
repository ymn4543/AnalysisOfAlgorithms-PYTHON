"""
CSCI-261 Analysis of Algorithms hw-4 problem 3
Youssef Naguib
ymn4543@rit.edu
"""
import sys

"""
alpha is a helper function for the headache problem. It calculates the
headache value of combining two employees based on their type. There are 3 types
V,E,N. An N and E pairing returns a headahc eof 5, any other combination returns 0.
"""
def alpha(char1,char2):
    if char1+char2 == "EN" or char1+char2 == "NE":
        return 5
    else:
        return 0


"""
min_headache calculates the minimum units of headache that can be incured while 
boarding all company employees on an amusement park ride.
param stringm: a string that represents line 1.
param stringn: a string that represents line 2.
"""
def min_headache(stringm,stringn):
    s = [[0 for x in range(len(stringn)+1)] for y in range(len(stringm)+1)] #i is y axis, j is x axis
    s[0][1] = 0     # BASE CASE
    s[1][0] = 0     # BASE CASE

    for i in range(2,len(stringm)+1):                               # BASE CASES FOR FIRST COLUMN
        s[i][0] = min(alpha(stringm[i-2],stringm[i-1])+s[i-2][0],
                            4 + s[i-1][0])

    for j in range(2,len(stringn)+1):                               # BASE CASES FOR FIRST ROW
        s[0][j] = min(alpha(stringn[j-2],stringn[j-1])+s[j-2][0],
                      4 + s[j-1][0])

    s[1][1] = min(alpha(stringm[0],stringn[0]),4)                   # BASE CASE FOR FIRST DIAGONAL

    for i in range(2,len(stringm)+1):        # BASE CASES FOR SECOND COLUMN (4 CHOICES)
        s[i][1] = min(s[i-1][0] + alpha(stringn[0],stringm[i-1]),  # take one from each line
                                alpha(stringm[i-1],stringm[i-2])+s[i-2][1]+3,  # take two from line m
                                4 + s[i][0],                                 # take one from line m
                                4 + s[i-1][1])                                 # take one from line n

    for j in range(2,len(stringn)+1):           # BASE CASES FOR SECOND ROW (4 CHOICES)
        s[1][j] = min(s[0][j-1] + alpha(stringn[j-1],stringm[0]),  # take one from each line
                      alpha(stringn[j-1],stringn[j-2])+s[1][j-2]+3,  # take two from line n
                      4 + s[0][j],                                 # take one from line m
                      4 + s[1][j-1])                                 # take one from line n

    # BASE CASES DONE

    # FILL IN REST OF M * N DYNAMIC ARRAY  (5 CHOICES FOR EACH)
    for i in range(2,len(stringm)+1):
        for j in range(2,len(stringn)+1):

            s[i][j] = min(s[i-1][j-1] + alpha(stringn[j-1],stringm[i-1]),  # take one from each line
                          alpha(stringm[i-1],stringm[i-2])+s[i-2][j]+3,  # take two from line m
                          alpha(stringn[j-1],stringn[j-2])+s[i][j-2]+3,  # take two from line n
                          4 + s[i-1][j],                                 # take one from line m
                          4 + s[i][j-1])                                 # take one from line n

    return s[len(stringm)][len(stringn)]    # return final value


"""
main function reads in input and runs the min headache algorithm, outputting
the result to the user.
"""
def main():
    m = int(sys.stdin.readline())   # number of employees in line 1
    n = int(sys.stdin.readline())   # number of employees in line 2
    line_1 = sys.stdin.readline().split()   # read in line 1
    line_2 = sys.stdin.readline().split()   # read in line 2
    stringm, stringn = "", ""
    for i in line_1:
        stringm += str(i)       # build stringm from line1
    for j in line_2:
        stringn += str(j)       # build stringn from line2
    print(min_headache(stringm,stringn))    # print answer
    return


if __name__ == '__main__':
    main()
