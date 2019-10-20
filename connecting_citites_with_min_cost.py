from collections import defaultdict

class Solution:
    '''Connecting Cities with Minimum Cost == Find Minimum Spanning Tree'''

    # def minimumCost(self, N, connections):
    #     '''
    #     Prim's Algorithm:
    #     1) Initialize a tree with a single vertex, chosen
    #     arbitrarily from the graph.
    #     2) Grow the tree by one edge: of the edges that
    #     connect the tree to vertices not yet in the tree,
    #     find the minimum-weight edge, and transfer it to the tree.
    #     3) Repeat step 2 (until all vertices are in the tree).
    #     '''
    #     # city1 <-> city2 may have multiple different cost connections,
    #     # so use a list of tuples. Nested dict will break algorithm.
    #     G = defaultdict(list)
    #     for city1, city2, cost in connections:
    #         G[city1].append((cost, city2))
    #         G[city2].append((cost, city1))
    #
    #     queue = [(0, N)]  # [1] Arbitrary starting point N costs 0.
    #     visited = set()
    #     total = 0
    #     while queue and len(visited) < N:  # [3] Exit if all cities are visited.
    #         # cost is always least cost connection in queue.
    #         cost, city = heapq.heappop(queue)
    #         if city not in visited:
    #             visited.add(city)
    #             total += cost  # [2] Grow tree by one edge.
    #             for edge_cost, next_city in G[city]:
    #                 heapq.heappush(queue, (edge_cost, next_city))
    #     return total if len(visited) == N else -1
    #

    def minimumCost(self, N, connections):
        '''
        Kruskal's Algorithm:
        1) Create a forest F (a set of trees), where each vertex in
        the graph is a separate tree.
        2) Create a set S containing all the edges in the graph.
        3) While S is nonempty and F is not yet spanning (fully connected):
            3A) Remove an edge with minimum weight from S
            3B) If the removed edge connects two different trees then
            add it to the forest F, combining two trees into a single tree.
        '''

        def find(city):
            # Recursively re-set city's parent to its parent's parent.
            # Build the bush: ideally each tree/set is of height 1.
            if parent[city] != city:
                parent[city] = find(parent[city])
            return parent[city]

        def union(c1, c2):
            root1, root2 = find(c1), find(c2)
            if root1 == root2:
                return False
            parent[root2] = root1  # Always join roots!
            return True

        # [1] Keep track of disjoint sets. Initially each city is its own set.
        parent = {city: city for city in range(1, N + 1)}
        # [2] Sort connections so we are always picking minimum cost edge.
        connections.sort(key=lambda x: x[2])
        total = 0
        for city1, city2, cost in connections:  # [3A]
            if union(city1, city2):  # [3B]
                total += cost
        # Check that all cities are connected.
        root = find(N)
        return total if all(root == find(city) for city in range(1, N + 1)) else -1

s = Solution()
n3 = 4
# city3 = [[1,2,1],[0,1,5],[0,2,6]]
city3 = [[0, 1, 3], [2, 3, 4]]
print(s.minimumCost(n3, city3))