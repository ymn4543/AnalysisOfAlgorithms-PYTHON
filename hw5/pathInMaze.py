"""
CSCI-261 Analysis of Algorithms hw-5 problem 1
Youssef Naguib
ymn4543@rit.edu
"""
import sys

"""
enqueue(): adds an element to the end of the queue, and marks
the relationship on the adjacency matrix.
param array: the queue
param element: element to be added to queue
param adj_matrix: the adjacency matrix to be updated
"""
def enqueue(array,element,adj_matrix):
    array.append(element)       # add element to back of queue
    x = element[0]
    y = element[1]
    adj_matrix[x][y] = 1        # update adjacency matrix


"""
check_directions(): checks all 4 directions in a maze. (North, South, East, West)
if they are valid spaces they are added to the queue and the numeber of possible moves
is increased.
param start: the coordinates of the current location in maze
param maze: a matrix representation of a maze
param queue: a queue data structure
param width: width of maze
param height: height of maze
param adj_matrix: the adjacency matrix 
"""
def check_directions(start,maze,queue,width,height,adj_matrix):
    #check 4 possible directions
    possibilities = 0
    #check north
    if start[0]-1>=0:
        if(maze[start[0]-1][start[1]]) != 1:
            north = [start[0]-1,start[1]]
            if adj_matrix[north[0]][north[1]]!=1:
                enqueue(queue,north,adj_matrix)
                possibilities+=1
    #check east
    if start[1]+1<width:
        if(maze[start[0]][start[1]+1]) != 1:
            east = [start[0],start[1]+1]
            if adj_matrix[east[0]][east[1]]!=1:
                enqueue(queue,east,adj_matrix)
                possibilities+=1
    #check south
    if start[0]+1<height:
        if(maze[start[0]+1][start[1]]) != 1:
            south = [start[0]+1,start[1]]
            if adj_matrix[south[0]][south[1]]!=1:
                enqueue(queue,south,adj_matrix)
                possibilities+=1
    #check west
    if start[1]-1>=0:
        if(maze[start[0]][start[1]-1]) != 1:
            west = [start[0],start[1]-1]
            if adj_matrix[west[0]][west[1]]!=1:
                enqueue(queue,west,adj_matrix)
                possibilities+=1
    return possibilities



"""
find_shortest_path(): finds the minimum number of moves required to get from a
starting coordinate to a destination coordinate in a maze.
param maze: matrix representation of a maze
param start: starting coordinate
param end: destination coordinate
param width: width of maze
param height: height of maze
"""
def find_shortest_path(maze,start,end,width,height):
    adj_matrix = [[0]*width for c in range(height)]
    # add start node to queue
    queue = []
    enqueue(queue,start,adj_matrix)
    possibilities = check_directions(start,maze,queue,width,height,adj_matrix)
    index = 1   # index in queue
    steps = 1   # number of steps to get to end
    neighbors = 0
    checkpoint = steps + possibilities # number of possibilities from one extra step
    while(index!=len(queue)):
        if index == checkpoint: # if all possibilities accounted for, take another step
            steps+=1
            checkpoint = index+neighbors
            neighbors = 0
        possibilities = check_directions(queue[index],maze,queue,width,height,adj_matrix)
        neighbors+=possibilities
        index+=1
        if adj_matrix[end[0]][end[1]] ==1:  # if destination reached, print steps
            print(steps+1)
            return
    print(-1)
    return



"""
main() reads in input including maze parameters, the maze itself, and
starting and ending nodes. It proceeds to call the find_shortest_path()
method and output the answer to the shortest path problem.
"""
def main():
    # read in input
    sizes = sys.stdin.readline().split()
    sizes = [int(x) for x in sizes]
    height = sizes[0]
    width = sizes[1]
    maze = [[0]*width]*height

    # read in maze
    for i in range(height):
        line = sys.stdin.readline().split()
        line = [int(x) for x in line]
        maze[i] = line

    start = [0,0]
    end= [0,0]

    # find start and end coordinates
    for i in range(width):
        for j in range(height):
            if maze[j][i] == 2:
                start = [j,i]
            if maze[j][i] == 3:
                end = [j,i]

    # find shortest path between them
    find_shortest_path(maze,start,end,width,height)



if __name__ == '__main__':
    main()
