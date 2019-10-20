''' https://www.youtube.com/watch?v=6j-vHQMXXiA '''

# Class to represent a graph
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary

    # to store graph

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # A utility function to find set of an element i
    # (uses path compression technique)
    def find(self, parent, i):
        #print("Inside find i : " + str(i) + " parent: " + str(parent))
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # The main function to construct MST using Kruskal's
    # algorithm
    def KruskalMST(self):

        result = []  # This will store the resultant MST

        i = 0  # An index variable, used for sorted edges
        e = 0  # An index variable, used for result[]

        # Step 1: Sort all the edges in non-decreasing
        # order of their
        # weight. If we are not allowed to change the
        # given graph, we can create a copy of graph
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = [];
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            # print(node)
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:

            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge does't cause cycle,
            # include it in result and increment the index
            # of result for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            # Else discard the edge

        # print the contents of result[] to display the built MST

        "Following are the edges in the constructed MST"
        cost = 0
        for u, v, weight in result:
            # print str(u) + " -- " + str(v) + " == " + str(weight)
            print("%d -- %d == %d" % (u, v, weight))
            cost += weight
        return cost

        # Driver code

def getMinCost(n, cities):
    g = Graph(n)
    for i in range(n):
        for j in range(i, n):
            if cities[i][j] == 0: continue
            g.addEdge(i,j,cities[i][j])
    #print(g.graph)
    print("Cost is : " + str(g.KruskalMST()))

# n1 = 5
# city1 = [[0, 1, 2, 3, 4], [1, 0, 5, 0, 7], [2, 5, 0, 6, 0], [3, 0, 6, 0, 0], [4, 7, 0, 0, 0]]
# getMinCost(n1,city1)
#
# n2 = 6
# city2 = [[0, 1, 1, 100, 0, 0], [1, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [100, 0, 0, 0, 2, 2], [0, 0, 0, 2, 0, 2], [0, 0, 0, 2, 2, 0]]
# getMinCost(n2,city2)

n3 = 3
#city3 = [[1,2,1],[0,1,5],[0,2,6]]
city3 = [[0,1,5],[0,2,6],[1,2,1]]
getMinCost(n3,city3)

n4 = 4
#city3 = [[1,2,1],[0,1,5],[0,2,6]]
city3 = [[0,1,3],[2,3,4]]
getMinCost(n3,city3)


# This code is contributed by Neelam Yadav
