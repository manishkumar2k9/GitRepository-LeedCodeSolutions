def longestPalindrome(s: str) -> str:
    res = s if len(s) == 1 else ""
    for i in range(len(s)):
        for j in range(len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                if len(res) < len(s[i:j]):
                    res = s[i:j]
    return res

def longestPalindrome_2(s: str) -> str:
    # mid, res = 0, None
    if len(s) == 1:
        return s
    mid = len(s)//2
    res = s[mid]
    i = 0
    while (mid + i >= 0 or mid - i < len(s)) and mid + i < len(s):
        print(" {} {} {} {}".format(str(mid),str(i), str(len(s)), res))
        if s[mid - i: mid + i] == s[mid -i: mid + i][::-1]:
            res = s[(mid - i): (mid + i)]
            print(" Here {} {} {} {}".format(str(mid), str(i), str(len(s)), res))
        else:
            if s[mid -i] == s[mid + i]:
                res = s[mid -i] + res + s[mid +i]
        i += 1
    return res

def expandAroundCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        #print("Inside s={} left={} right={} s[left]={} s[right]={}  ".format(s, str(left), str(right), s[left], s[right]))
        left -= 1
        right += 1
    ret = right - left - 1
    print("Inside s={} left={} right={} ret={}".format(s, str(left), str(right), str(ret)))
    return ret

def leetCodeSolution(s):
    start, end = 0, 0
    for i in range(len(s)):
        len1 = expandAroundCenter(s, i, i)
        len2 = expandAroundCenter(s, i, i +1)
        len3 = max(len1, len2)
        if len3 > end - start:
            start = i - (len3 -1)//2
            end = i + len3//2
        print("start {} end {} i {} len3 {} ".format(str(start),str(end),str(i), str(len3)))
    return s[start:end+1]

## For this input, the performance is very bad.. O(n^3)

s = "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
res = s if len(s) <= 1 else ""
for i in range(len(s)):
    # print(" i " + str(i))
    for j in range(len(s)+1):
        # print(" j " + str(j))
        # print(" {} and {} ".format(s[i:j],s[i:j][::-1]))
        if s[i:j] == s[i:j][::-1]:
            if len(res) < len(s[i:j]):
                res = s[i:j]
        else:
             print(" Outside {} --> {} ".format(s[i:j], s[i:j][::-1]))

print(leetCodeSolution("abcbcdefg"))