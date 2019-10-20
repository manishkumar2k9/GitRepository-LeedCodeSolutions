def binary_search(list, target):
    low = 0
    high = len(list) -1
    while low <= high:
        mid = (low + high)//2
        if list[mid] > target:
            high = mid -1
        elif list[mid] < target:
            low = mid + 1
        else:
            return True
    return False

def searchMatrix(matrix, target):
    for i in range(len(matrix)):
        row = matrix[i]
        col = [matrix[j][i] for j in range(i,len(matrix))]
        # for j in range(i,len(matrix)):
        #     col = matrix[j][i]
        if binary_search(row, target) or binary_search(col, target):
            return True
    return False

matrix = [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

target = 35
print(searchMatrix(matrix, target))