def minCost(cities, n):
    weighted_list = {}
    spanning_tree_count = 0
    cost = 0
    source = []
    destination = {}
    for i in range(n):
        for j in range(i,n):
            #print(str(i) + "," + str(j))
            if cities[i][j] == 0: continue
            weight = cities[i][j]
            if weight in weighted_list:
                weighted_list[weight] = weighted_list[weight] + [i,j]
            else:
                weighted_list[weight] = list([i,j])
    for w in sorted(weighted_list):
        for connted_cities_list in weighted_list[w]:
            for i in range(0,len(list(connted_cities_list)),2):
                if (connted_cities_list[i] or connted_cities_list[i+1]) in destination:
                    continue
                else:
                    destination[i] = True
                    cost += w
    print(cost)




    # while spanning_tree_count < n -1:
    #     cost += sorted_spanning_cost[spanning_tree_count]
    #     spanning_tree_count += 1
    # print(cost)
    sorted(weighted_list)
    print(weighted_list)
    #print(new_sorted_list)
    return "minCost"


print("Inside main ")
# n1 = 5
# city1 = [[0, 1, 2, 3, 4], [1, 0, 5, 0, 7], [2, 5, 0, 6, 0], [3, 0, 6, 0, 0], [4, 7, 0, 0, 0]]
# print(minCost(city1,n1))

#  Input 2
n2 = 6
city2 = [[0, 1, 1, 100, 0, 0], [1, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [100, 0, 0, 0, 2, 2], [0, 0, 0, 2, 0, 2], [0, 0, 0, 2, 2, 0]]
print(minCost(city2,n2))
print("Main complete !")
