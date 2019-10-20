from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]
ans = defaultdict(list)
for s in strs:
    #print(sorted(s))
    ans[tuple(sorted(s))].append(s)

print(list(ans.values()))


