'''page 59 of interview python'''

import random

def offline_sampling(k, A):
    for i in range(k):
        # Generate a random index between i to len(A) -1
        r = random.randint(i,len(A)-1)
        A[i],A[r] = A[r],A[i]
    return A

inlist = [3,7,5,11]
print(offline_sampling(2, inlist))