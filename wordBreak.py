def call_recursive_solution(s, workList):
    return recursive_solution(s, workList, 0, [])

def recursive_solution(s, workList, start, words):
    print(" start:{} str: {}".format(str(start), s))
    if s == None:
        return True
    if s in workList:
        words.append(s)
        return True
    for i in range(start+1, len(s)+1):
        print(s[:i])
        if s[:i] in workList and recursive_solution(s[i:],workList, i, words):
            words.append(s[:i])
            #return True
    return words


def dp_solution(s, wordList):
    dp = [ None for i in range(len(s) + 1) ]
    #if s[0] in wordList:
    dp[0] = True

    for i in range(1,len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordList:
                dp[i] = True
    print(dp)
    return dp[len(s)]

dictL = {}
s = "code"
wordList = ["c","od","e","x"]

s = "leetcode"
wordList = ["leet","code"]

s = "IAmAce"
wordList = ["I", "Am", "Ace"]

s="catsanddog"
wordList =["cat","cats","and","sand","dog"]

#print(dp_solution(s, wordList))
print(call_recursive_solution(s, wordList))