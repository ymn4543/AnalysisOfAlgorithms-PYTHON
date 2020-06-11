"""
CSCI-261 Analysis of Algorithms hw-5 problem 2
Youssef Naguib
ymn4543@rit.edu
"""
import sys

"""
reverse_graph(): reverses a directed graph, returns the inverse
adjacency matrix.
param adj: adjacency matrix of directed graph
"""
def reverse_graph(adj):
    inverse = [[]for i in range(len(adj))]
    index = 1
    for v in range(len(adj)):
        items = adj[v]
        for i in items:
            if i!=0:
                inverse[i-1].append(index)
        index +=1
    for i in inverse:
        i.append(0)
    return inverse


"""
process_by_finish_time(): orders vertices by reverse finishing time.
(highest finishing times first).
param finish: array of finish times
"""
def process_by_finish_time(finish):
    vertices_by_fin_time = [0]*len(finish)
    for i in range(len(finish)):
        vertices_by_fin_time[finish[i]-1] = i
    vertices_by_fin_time.reverse()
    return vertices_by_fin_time


"""
DFS(): implementation of depth first search
param seen: array of seen vertices
param start_node: starting location of search
param list: adjacency list of directed graph
param time: current time (depth)
param finish: array of finish times
"""
def DFS(seen,start_node,list,time,finish):
    seen[start_node] = True
    vertex = list[start_node]
    for neighbor in vertex:
        if neighbor!=0 and seen[neighbor-1] == False:
            time = DFS(seen,neighbor-1,list,time,finish)
    time+=1
    finish[start_node]=time
    return time


"""
iterative_DFS(): is an iterative implementation of depth first search.
param seen: array of seen vertices
param start_node: starting location of search
param list: adjacency list of directed graph
"""
def iterative_DFS(seen,start_node,list):
    stack = []
    new = [start_node]
    stack.append(start_node)
    while (len(stack)!=0):
        top = stack.pop()
        seen[top] = True
        neighbors = list[top]
        for n in neighbors:
            if n!=0 and seen[n-1] == False:
                stack.append(n-1)
                new.append(n-1)
    return new


"""
construct_DAG(): constructs a directed acylic graph (DAG),
given strongly connected components and a directed graph.
param mini_v: array of arrays. Each subarray is a collection of nodes in same 
              strongly connected component.
param list: adjacency list of directed graph              
"""
def construct_DAG(mini_v,list):
    index_of_each = [0]*len(list)
    for v in range(len(mini_v)):
        for m in mini_v[v]:
            index_of_each[m]=v

    adjacency_list =  [[0]*len(mini_v) for i in range(len(mini_v))]
    l = 0
    for v in mini_v:                        # build matrix of DAG
        for number in v:
            neighbors = list[number]
            for n in neighbors:
                if n !=0:
                    c = index_of_each[n-1]
                    if l !=c:
                        adjacency_list[l][c] = 1
        l+=1

    find_min_number_edges_needed(adjacency_list)    #  find min number of edges to make DAG strongly connected


"""
find_min_number_edges_needed(): finds the number of edges required for a DAG
to become strongly connected.
param adjacency_list: adjacency list representation of DAG
"""
def find_min_number_edges_needed(adjacency_list):
    out_degree_0 = 0                    # number of nodes with out-degree of 0

    for node in adjacency_list:
        if is_all_0(node):
            out_degree_0+=1

    num_nodes = len(adjacency_list)
    incoming = [0] * num_nodes
    in_degree_0 = 0                     # number of nodes with in-degree of 0
    for node in adjacency_list:
        for a in range(len(node)):
            if node[a] ==1:
                incoming[a]=1
    for v in incoming:
        if v ==0:
            in_degree_0+=1

    answer = max(in_degree_0,out_degree_0)  # the answer is always the max of these 2 values

    if answer == 1:                         # if answer is 1, only one edge needed, print YES
        print("YES")
    else:
        print ("NO")

    return


"""
is_all_0(): returns true if list contains only 0's
param list: array of integers
"""
def is_all_0(list):
    nonzeros = 0
    for i in list:
        if i!=0:
            nonzeros+=1
    return nonzeros==0


"""
strongly_connected_componants(): finds the number of strongly connected
components in a directed graph, and their corresponding vertices.
It then calls construct_DAG to create a "mini-version" where each strongly
connected component is a single vertex. 
param list: the adjacency list of the directed graph
"""
def strongly_connected_componants(list):
    seen,finish = [],[]
    for vertex in list:
        seen.append(False)
        finish.append(None)
    time = 0
    for vertex in range(len(list)):             # run dfs on every node to find finish times
        if seen[vertex]==False:
            time = DFS(seen,vertex,list,time,finish)
    reverse_list = reverse_graph(list)              # reverse graph
    sorted_fins = process_by_finish_time(finish)    # sort by finish times
    for i in range(len(seen)):
        seen[i] = False

    scc = 0
    mini_v = []
    for vertex in sorted_fins:
        if seen[vertex] == False:
            k = iterative_DFS(seen,vertex,reverse_list)     # run dfs on reverse graph
            scc +=1                                         # count number of strongly connected components
            mini_v.append(k)                                # build list of vertices for each component
    construct_DAG(mini_v,list)                              # build a DAG out of all strongly connected components
    return


"""
main function reads in input representing a directed graph.
it then calls functions that decide if this graph can become strongly
connected with the addition of a single edge.
"""
def main():
    nodes = int(sys.stdin.readline())       # read in number of nodes
    adjacency_list = []
    for i in range(nodes):      # read in adjacency list
        list = sys.stdin.readline().split()
        list = [int(x) for x in list]
        adjacency_list.append(list)

    # run the algorithm
    strongly_connected_componants(adjacency_list)



if __name__ == '__main__':
    main()
