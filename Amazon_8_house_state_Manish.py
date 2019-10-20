def cellComplete(cells, days):
    first_neighbour, last_neighbour = 0 , 0
    newCells = list(cells)
    for _ in range(inDays):
        for j in range(len(cells)):
            if j == 0:
                #newCells[j] = (first_neighbour ^ cells[j] ^ cells[j+1])
                newCells[j] = 1 - (first_neighbour == cells[j + 1])
                # print(str(j) + " newCells[j] " + str(newCells[j]))
            elif j == len(cells) -1:
                # newCells[j] = (cells[j-1] ^ cells[j] ^ last_neighbour)
                newCells[j] = 1 - (cells[j - 1] == last_neighbour)
                # print(str(j) + " newCells[j] " + str(newCells[j]))
            else:
                # newCells[j] = (cells[j-1] ^ cells[j] ^ cells[j+1])
                newCells[j] = 1 - (cells[j - 1] == cells[j + 1])
                # print(str(j) + " newCells[j] " + str(newCells[j]))
        cells = newCells[:]
    print(newCells)
    return "Done"

inCells = [1, 0, 0, 0, 0, 1, 0, 0]
inDays = 1

# inCells = [1, 1, 1, 0, 1, 1, 1, 1]
# inDays = 2

print(cellComplete(inCells,inDays))