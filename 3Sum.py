class Solution:
    def threeSum(self, nums):
        nums.sort()
        print(nums)
        outPut_List = []
        for i in range(len(nums) -2):
            ## This if block is handle duplicates.
            if i == 0 or (nums[i] != nums[i-1]):
                low = i + 1
                high = len(nums) -1
                sum = 0 - nums[i]
                while low < high:
                    if nums[low] + nums[high] == sum:
                        outPut_List.append([nums[i],nums[low],nums[high]])
                        # This block is to make sure we are not checking same number in low and high sides.
                        while low < high and nums[low] == nums[low+1]:
                                low +=1
                        while low < high and nums[high] == nums[high-1]:
                            high -= 1
                        low += 1
                        high -= 1
                    elif nums[low] + nums[high] > sum:
                        high -= 1
                    else:
                        low += 1
        return outPut_List

s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))