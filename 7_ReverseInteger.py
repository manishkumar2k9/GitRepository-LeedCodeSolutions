import math
import sys

class Solution:
    def reverse(self, x: int) -> int:
        result, remain = 0, abs(x)
        intMaxValue = sys.maxsize
        intMinValue = -sys.maxsize - 1
        while remain:
            result = result * 10 + remain % 10
            remain //= 10
            if (result > intMaxValue//10) | ((result == intMaxValue//10) & (remain == 7)):
                #print(" gt" + str(result))
                return 0
            if (result < intMinValue//10) | ((result == intMinValue//10) & (remain == 8)):
                #print(" ls" + str(result))
                return 0
        return -result if (x < 0) else result

s1 = Solution()
print(s1.reverse(1534236469))
print(s1.reverse(1534))
print(s1.reverse(-7483412))

