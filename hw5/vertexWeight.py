"""
CSCI-261 Analysis of Algorithms hw-5 problem 4
Youssef Naguib
ymn4543@rit.edu
"""
import sys

"""
update(): updates the distance to a node if it is optimal.
param weights: weights of all nodes stored in array
param edges: array of all edges
param node: start node
param parent: array of node parents
"""
def update(weights,edges,node,dist,parent):
    neighbors = edges[node]
    for v in neighbors:
            if dist[v] > dist[node] + weights[v]:
                dist[v] = dist[node] + weights[v]
                parent[v] = node


"""
dijkstra(): finds minimum cost path from w starting node to all other nodes.
Nodes have a positive weight.
param weights: weights of all nodes stored in array
param edges: array of all edges
param start: start node
param num_nodes: the number of nodes in the graph
"""
def dijkstra(weights,edges,start,num_nodes):
    H = []
    for i in range(num_nodes):
        if i != start:
            H.append(i)
    dist,parent = [0 for i in range(num_nodes)],[0 for i in range(num_nodes)]
    for v in range(num_nodes):
        dist[v] = float("inf")
        parent[v] = None
    dist[start] = weights[start]
    parent[start] = None
    update(weights,edges,start,dist,parent)
    for i in range(1,num_nodes-1):
        min = float("inf")
        min_index = float("inf")
        for l in H:
           x = dist[l]
           if x < min:
               min = x
               min_index = l
        update(weights,edges,min_index,dist,parent)
        del H[H.index(min_index)]

    return dist


"""
main(): reads in input of node weights, and edges that exist.
runs djikstra to calculate min cost for given start node to reach all
other nodes. Displays result to output.
"""
def main():
    sizes = sys.stdin.readline().split()
    sizes = [int(x) for x in sizes]
    num_nodes = sizes[0]
    num_edges = sizes[1]
    weights = sys.stdin.readline().split()
    weights = [int(x) for x in weights]
    edges = [[]for i in range(num_nodes)]
    for i in range(num_edges):
        list = sys.stdin.readline().split()
        list = [int(x) for x in list]
        start = list[0]-1
        end = list[1]-1
        edges[start].append(end)
        edges[end].append(start)

    start = int(sys.stdin.readline())-1
    x = dijkstra(weights,edges,start,num_nodes)
    answer = ""
    for num in x:
        answer += str(num) + " "
    print (answer)



if __name__ == '__main__':
    main()
