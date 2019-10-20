''' page no. 58 of Interview in python'''
def next_permutation(perm):
    inversion_point = len(perm) - 2
    while ((inversion_point >= 0) and (perm[inversion_point] > perm[inversion_point+1])):
        inversion_point -= 1

    if inversion_point == -1:
        return []

    for i in reversed(range(inversion_point + 1, len(perm))):
        print("Inversion revered " + str(i))
        if perm[i] > perm[inversion_point]:
            perm[i], perm[inversion_point] = perm[inversion_point], perm[i]
            break

    print("Inside : " + str(perm))
    perm[inversion_point + 1:] = reversed(perm[inversion_point + 1:])
    #inversion_point -= 1
    return perm

nlist = [6,2,1,5,4,3,0]
print("Input :  " + str(nlist))
print(next_permutation(nlist))