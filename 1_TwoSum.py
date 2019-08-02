class Solution:
    " BRUTE-FORCE solution"
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return [-1,-1]

    def twoSumDict(self, nums, target) -> list:
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = i
        for i in range(len(nums)):
            if ((target - nums[i]) in dict) and (dict[target - nums[i]] != i):
                return [i,dict[target - nums[i]]]
        return [-1,-1]


inList = [3,2,4]

s1 = Solution()
print(s1.twoSum(inList,9))
print(s1.twoSumDict(inList,6))