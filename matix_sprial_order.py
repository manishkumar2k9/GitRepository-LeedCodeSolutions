def matrix_in_spiral_order(square_matrix):
    shift = ((0,1),(1,0),(0,-1),(-1,0))
    direction = x = y = 0
    spiral_ordering = []

    for i in range(len(square_matrix)**2):
        spiral_ordering.append(square_matrix[x][y])
        square_matrix[x][y] = 0
        next_x, next_y = x + shift[direction][0], y + shift[direction][1]
        print("next_x : " + str(next_x) + " next_y :" + str(next_y) + " Value : " + str(i))
        if(next_x not in range(len(square_matrix))
            or next_y not in range(len(square_matrix))
            or square_matrix[next_x][next_y] == 0
          ):
            print("Before Inside: " + str(next_x) + " " + str(next_y) + " " + str(direction))
            direction = (direction + 1) & 3
            print("Inside: " + str(next_x) + " " + str(next_y) + " " + str(direction))
            next_x, next_y = x + shift[direction][0], y + shift[direction][1]
        x, y = next_x, next_y
    return spiral_ordering


# square_matrix = [[1,2,3],[4,5,6],[7,8,9]]
square_matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(len(square_matrix))
print(matrix_in_spiral_order(square_matrix))