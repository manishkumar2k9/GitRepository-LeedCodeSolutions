import time

def binarySearchFirst(list, target) -> int:
    low, high, result = 0, len(list) - 1, -1

    while low <= high:
        mid = (low + high) // 2
        if list[mid] == target:
            result = mid
            high = mid - 1
        elif list[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return result

t0 = time.time()
#inList = [ x for x in range(10000000)]
inList = [1,2,2,3,3,5,5,5,5,5,9,9,11,11]
print(binarySearchFirst(inList,5))
t1 = time.time()
print(t1-t0)