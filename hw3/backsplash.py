"""
Author: Youssef Naguib <ymn4543@rit.edu>
CSCI-261 hw-3 question 5 implementation
"""
import sys

"""
this algorithm calculates the number of possible ways a backsplash
wall can be covered using 1x1 and 2x2 (L-shaped missing corner) tiles.
The answer depends on smaller problems, and builds up to the final solution.
"""
def possible_tiles(tile_list,wall_width):
    for i in range(3,wall_width+1):      # iterate up to the final answer (index represents dimensions/2)
        tile_list[i] = (tile_list[i-1]) + (4 * tile_list[i-2]) + (2 * tile_list[i-3])
    return tile_list[i]              # a backsplash of size 2 x n can be formed (n-1) + 4(n-2) + 2(n-3) ways

def main():
    wall_width = int(sys.stdin.readline())      # a backsplash has dimensions 2 x n , this value represents n
    tile_list = [0] * (wall_width+1)            # initialize dynamic array of size n
    tile_list[0] = 1                            # fill in 3 base cases into array
    tile_list[1] = 1
    tile_list[2] = 5
    possibilities = possible_tiles(tile_list, wall_width)   # calculate possible combinations of tiles
    print(possibilities)                                    # print result
    return                                                  # end of program

if __name__ == '__main__':
    main()
