A = [9,9,9]
#print(A[-1])
A[-1] += 1
print(A)
for i in reversed(range(1,len(A))):
    if A[i] != 10:
        break
    A[i] = 0
    A[i -1] += 1
    print(A)
if A[0] == 10:
    A[0] = 1
    A.append(0)
print(A)