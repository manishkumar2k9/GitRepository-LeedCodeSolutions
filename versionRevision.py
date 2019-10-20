def version_revision(v1, v2):
    maxSize = max(len(v1), len(v2))
    v1_list = [ 0 for i in range(maxSize)]
    v2_list = [ 0 for i in range(maxSize)]

    #v1_list = [ v1_list[i] for i in v1.split('.') ]
    #v2_list = [ v2_list[i] for i in v2.split('.') ]

    for i,val in enumerate(v1.split('.')):
        v1_list[i] = int(val)

    for i,val in enumerate(v2.split('.')):
        v2_list[i] = int(val)

    for i in range(maxSize):
        if v1_list[i] > v2_list[i]:
            return 1
        elif v1_list[i] < v2_list[i]:
            return -1
        else:
            continue
    return 0


v1 = "1.0"
v2 = "1"
print(version_revision(v1, v2))