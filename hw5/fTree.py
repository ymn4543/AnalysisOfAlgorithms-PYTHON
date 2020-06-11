"""
CSCI-261 Analysis of Algorithms hw-5 problem 3
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
        if array1[0][2] > array2[0][2]:                   # if array1 first value greater than array2 first value
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
init(): initializes the union-find data structure
param num_nodes: the number of vertices in the graph
"""
def init(num_nodes):
    boss, size, set = [],[],[]
    for v in range(num_nodes):
        boss.append(v)
        size.append(1)
        set.append([v])
    return boss,size,set


"""
find(): finds the boss of a vertex in the union find data struct
param u: vertex
param boss: array of bosses
"""
def find(u,boss):
    return boss[u]


"""
union(): merges subsets of 2 vertices in the union-find data structure
param u: vertex 1
param v: vertex 2
param boss: array of bosses
param size: array of sizes
param set: array of sets
"""
def union(u,v,boss,size,set):
    if size[boss[u]]>size[boss[v]]:
        set[boss[u]] += (set[boss[v]])
        size[boss[u]]+=size[boss[v]]
        for z in set[boss[v]]:
            boss[z] = boss[u]
    else:
        set[boss[v]]+=(set[boss[u]])
        size[boss[v]]+=size[boss[u]]
        for z in set[boss[u]]:
            boss[z] = boss[v]



"""
kruskal(): is a modified version of kruskal's algorithm to account for edges that
must be part of a spanning tree. (Result may not be a minimal spanning tree because of this)
The algorithm returns the cost/weight associated with the minimal F-spanning tree.
F represents the set of edges that must be included.
param edges: set of edges in the graph
param ftree: set of edges that must be included
param num_nodes: number of vertices in graph
"""
def kruskal(edges,ftree,num_nodes):
    T = []                      # the set of edges in the spanning tree
    edges = merge_sort(edges)           # merge the edges by increasing weight
    boss,size,set = init(num_nodes)     # initialize union find data structure
    for edge in ftree:                  # first add all required edges to the union-find data structure
        if find(edge[0],boss) == find(edge[1],boss):
            print (-1)
            return
        u = edge[0]
        v = edge[1]
        union(u,v,boss,size,set)
        T.append(edge)                  # also add to spanning tree
    for edge in edges:              # then proceed with normal kruskal using remaining edges
        if find(edge[0],boss) != find(edge[1],boss):
            if edge not in T:
                T.append(edge)
                union(edge[0],edge[1],boss,size,set)
    total = 0
    for edge in T:          # add up total cost of spanning tree
        total+=edge[2]
    print(total)            # print to output and return
    return




"""
main(): reads in input and calls kruskal algorithm to determine
cost of minimal spanning tree that includes all edges in the set F.
"""
def main():
    sizes = sys.stdin.readline().split()
    list = [int(x) for x in sizes]
    num_nodes = list[0]
    num_edges = list[1]
    f_tree = []
    edges = []
    for e in range(num_edges):
        edge = sys.stdin.readline().split()
        edge = [int(x)for x in edge]
        if edge[3]==1:
            f_tree.append(edge)
        edges.append(edge)
    kruskal(edges,f_tree,num_nodes)




if __name__ == '__main__':
    main()
