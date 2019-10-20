def can_reach_end(A):
    furthest_reach_so_far, last_index = 0, len(A) - 1
    i = 0
    while i <= furthest_reach_so_far and i <= last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, A[i])
        print(str(A[i]) + " " + str(furthest_reach_so_far))
        i += 1
    return furthest_reach_so_far >= last_index

listA = [3,3,1,0,2,0,1]
print(can_reach_end(listA))