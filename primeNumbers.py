n = 18

primes = []
is_prime = [False, False] + [True] * (n-1)
print(is_prime)

for i in range(2,n-1):
    if is_prime[i]:
        primes.append(i)
        for j in range(i*2, n-1, i):
            #print(j)
            is_prime[j] = False
#print(is_prime)
print(primes)  ## Time complexity is O(nlog logn)
