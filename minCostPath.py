def minCostPath(matrix, m, n):
    minCostPathMatrix = [[0 for x in range(m+1)] for y in range(n+1)]
    minCostPathMatrix[0][0] = matrix[0][0]
    for i in range(1,m+1):
        aboveCost = minCostPathMatrix[i-1][0]
        minCostPathMatrix[i][0] = aboveCost + matrix[i][0]

    for j in range(n+1):
        rightCost = minCostPathMatrix[0][j-1]
        minCostPathMatrix[0][j] = rightCost + matrix[0][j]

    for i in range(1,m+1):
        for j in range(1, n+1):
            minCostPathMatrix[i][j] = matrix[i][j] + min(minCostPathMatrix[i-1][j],minCostPathMatrix[i][j-1],minCostPathMatrix[i-1][j-1])
    print(minCostPathMatrix)
    return minCostPathMatrix

matrix = [[2,3,4],[5,9,8],[7,2,1]]
print("Original Matrix") #+ str(matrix))
for mt in matrix:
    print(mt)
newMat = minCostPath(matrix,2,2)
print("Min Cost Path for (2,2) is " + str(newMat[2][1]))
#newMatrix = [[0 for x in range(2+1)] for y in range(2+1)]
#print(newMatrix)