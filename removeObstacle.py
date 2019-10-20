import queue

def isGridValidNotVisted(nr, nc, x, y, vistedList):
    if x < 0 or y < 0 or x >= nr or y >= nc:
        return False
    if vistedList[x][y] is True:
        return False
    return True


def removeObstacle(nr, nc, grid):
    vistedList = [ [i for i in range(nc)] for j in range(nr)]
    for i in range(nr):
        for j in range(nc):
            if grid[i][j] == 0:
                vistedList[i][j] = True
            else:
                vistedList[i][j] = False

    q = queue.Queue()
    q.put((0, 0, 0))

    vistedList[0][0] = True
    while not q.empty():
        (current_x, current_y, current_dist) = q.get()
        #print(current_x, current_y, current_dist,vistedList[current_x-1][current_y])
        if grid[current_x][current_y] == 9:
            return current_dist

        #Moving Up
        if isGridValidNotVisted(nr,nc,current_x-1,current_y,vistedList):
            q.put((current_x-1,current_y,current_dist+1))
            vistedList[current_x-1][current_y] = True

        #Moving Down
        if isGridValidNotVisted(nr,nc,current_x+1,current_y,vistedList):
            q.put((current_x+1,current_y,current_dist+1))
            vistedList[current_x+1][current_y] = True

        #Moving Left
        if isGridValidNotVisted(nr,nc,current_x,current_y-1,vistedList):
            q.put((current_x,current_y-1,current_dist+1))
            vistedList[current_x][current_y-1] = True

        #Moving Right
        if isGridValidNotVisted(nr,nc,current_x,current_y+1,vistedList):
            q.put((current_x,current_y+1,current_dist+1))
            vistedList[current_x][current_y+1] = True
    return -1


grid = [[1, 1, 1, 1],
        [0, 1, 1, 1],
        [0, 1, 0, 1],
        [1, 1, 9, 1],
        [0, 0, 1, 1]]
print(removeObstacle(5,4,grid))

grid2 = [[1, 0, 0],
        [1, 0, 0],
        [1, 9, 0]]
print(removeObstacle(3,3,grid2))