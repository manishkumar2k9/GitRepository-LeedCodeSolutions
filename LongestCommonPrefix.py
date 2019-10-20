class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        if len(strs) == 1: return strs[0]

        for i,j in zip(strs[0], strs[-1]):
            print(str(i) + " -> " + str(j))
        print(strs.sort())

        strs.sort()
        p = ""
        for x, y in zip(strs[0], strs[-1]):
            if x == y:
                p += x
            else:
                break
        return p

    def longestCommonPrefix_2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        output = ""
        if strs is None or len(strs) == 0:
            return output

        index = 0
        for c in strs[0]:
            print(c)
            for i in range(1,len(strs)):
                if index >= len(strs[i]) or c != strs[i][index]:
                    return output
            output += c
            index += 1
        return output

s = Solution()

print(s.longestCommonPrefix(["flower","flow","flight"]))
