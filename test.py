import queue


def isGridValidNotVisted(nr, nc, x, y, vistedList):
    if x < 0 or y < 0 or x >= nr or y >= nc:
        return False
    if vistedList[x][y] is True:
        return False
    return True


def removeObstacle(numRows, numColumns, lot):
    # WRITE YOUR CODE HERE
    vistedList = [[i for i in range(numColumns)] for j in range(numRows)]
    for i in range(numRows):
        for j in range(numColumns):
            if lot[i][j] == 0:
                vistedList[i][j] = True
            else:
                vistedList[i][j] = False

    q = queue.Queue()
    q.put((0, 0, 0))
    vistedList[0][0] = True
    counter = 0
    while not q.empty():
        (current_x, current_y, current_dist) = q.get()
        print(current_x, current_y, current_dist, vistedList[current_x][current_y])
        if lot[current_x][current_y] == 9:
            return current_dist

        # Moving up
        if isGridValidNotVisted(numRows, numColumns, current_x - 1, current_y, vistedList):
            q.put((current_x - 1, current_y, current_dist + 1))
            vistedList[current_x - 1][current_y] = True

        # Moving down
        if isGridValidNotVisted(numRows, numColumns, current_x + 1, current_y, vistedList):
            q.put((current_x + 1, current_y, current_dist + 1))
            vistedList[current_x+1][current_y] = True

        # Moving left
        if isGridValidNotVisted(numRows, numColumns, current_x, current_y - 1, vistedList):
            q.put((current_x, current_y - 1, current_dist + 1))
            vistedList[current_x][current_y-1] = True

        # Moving right
        if isGridValidNotVisted(numRows, numColumns, current_x, current_y + 1, vistedList):
            q.put((current_x, current_y + 1, current_dist + 1))
            vistedList[current_x][current_y+1] = True
    return -1

grid2 = [[1, 0, 0],
        [1, 0, 0],
        [1, 9, 0]]
print(removeObstacle(3,3,grid2))