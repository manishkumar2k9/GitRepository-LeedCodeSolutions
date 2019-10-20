def getValue(inList, target)->list:

    hashMap = {}

    for i in range(len(inList)):
        calV = target - inList[i]
        if calV in hashMap:
            print("Output " + str(hashMap[calV]) + "," + str(i))
            return [hashMap[calV],i]
        else:
            hashMap[inList[i]] = i
    return -1

print(getValue([100,180,40,120,10],220))
print(getValue([1,10,25,35,60],60))

if any (
    ["HI" for j in range(5)
     for i in range(5)]
    ):
    print("Hello")