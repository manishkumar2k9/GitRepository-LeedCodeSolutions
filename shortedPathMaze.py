# import queue
#
# def solution(matrix, m, n):
#     vistedList = [[0 for x in range(m)] for y in range(n)]
#     name_queue = queue.Queue
#     for x in range(m+1):
#         for y in range(n+1):
#             currentCell = matrix[x][y]
#             if x < 0 ^ y < 0: continue
#             if (x > m) ^ (y > n) : continue
#             leftCell = matrix[x][y-1]
#             rightCell = matrix[x][y+1]
#             upCell = matrix[x-1][y]
#             downCell = matrix[x+1][y]
#             print("    " + str(upCell))
#             print(str(leftCell) + " " + str(currentCell)+ " " + srt(rightCell))
#             print("    " + str(downCell))
#
#     print(vistedList)
#     return 0


inputMatrix = [[1,0,0],
               [1,0,0],
               [1,9,1]]
# print(inputMatrix)
# print(solution(inputMatrix,3,3))

print(inputMatrix.remove())
