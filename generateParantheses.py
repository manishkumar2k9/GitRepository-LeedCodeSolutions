# def generate(A=[]):
#     if len(A) == (2*n):
#         if valid(A):
#             ans.append("".join(A))
#     else:
#         A.append('(')
#         print("1. calling generate")
#         generate()
#         print(A)
#         print("1. calling pop")
#         A.pop()
#         A.append(')')
#         print("2. calling generate")
#         generate()
#         print(A)
#         print("2. calling pop")
#         A.pop()
#         print(A)
#
# def valid(A):
#     bal = 0
#     for i in A:
#         if i == '(':
#             bal += 1
#         else:
#             bal -= 1
#     if bal < 0:
#         return False
#     return bal == 0
#
# n = 2
# ans = []
# generate()
# print(ans)



class Solution(object):
    def generateParenthesis(self, N):
        print("1. N: " + str(N))
        if N == 0: return ['']
        ans = []
        for c in range(N):
            for left in self.generateParenthesis(c):
                print("left " + str(left))
                for right in self.generateParenthesis(N-1-c):
                    print("right " + str(right))
                    ans.append('({}){}'.format(left, right))
        return ans

s = Solution()
print(s.generateParenthesis(2))