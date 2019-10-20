def minnode(n, keyval, mstset):
    mini, mini_index = 9999999999999, -1
    for i in range(n):
        if mstset[i] is False and keyval[i] < mini:
            mini = keyval[i]
            mini_index = i
    #print("Inside minnode " + str(mini) + " return mini_index " + str(mini_index))
    return mini_index


def findcost(n, city):
    # Array to store the parent # node of a particular node.
    parent, keyval, mstset = [0] * n, [None] * n, [None] * n
    for i in range(n):
        keyval[i] = 9999999999999
        mstset[i] = False
        parent[0] = -1
        keyval[0] = 0
        for j in range(n - 1):
            u = minnode(n, keyval, mstset)
            mstset[u] = True
            for v in range(n):
                if (city[u][v] and mstset[v]) is False and city[u][v] < keyval[v]:
                    keyval[v] = city[u][v]
                    parent[v] = u
    cost = 0
    for z in range(1, n):
        cost += city[parent[z]][z]
    print(cost)
    return "Done"


n1 = 5
city1 = [[0, 1, 2, 3, 4], [1, 0, 5, 0, 7], [2, 5, 0, 6, 0], [3, 0, 6, 0, 0], [4, 7, 0, 0, 0]]
print(findcost(n1, city1))

#  Input 2
n2 = 6
city2 = [[0, 1, 1, 100, 0, 0], [1, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [100, 0, 0, 0, 2, 2], [0, 0, 0, 2, 0, 2], [0, 0, 0, 2, 2, 0]]
print(findcost(n2, city2))
# This code is contributed by PranchalK [tabbyending]