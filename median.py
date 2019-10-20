def median(list):
    list.sort()
    if len(list) % 2 != 0:
        middle = int((len(list) - 1)/2)
        return list[middle]
    elif len(list) % 2 == 0:
        mid1 = int(len(list) / 2)
        mid2 = mid1 -1
        print(list[mid1])
        print(list[mid2])
        return (list[mid1] + list[mid2]) / 2

print(median([3]))