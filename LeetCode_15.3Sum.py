class Solution():

    def threeSum(self, nums):
        nums.sort()
        outputList = []
        for i in range(len(nums) -2):
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                low = i + 1
                high = len(nums) -1
                sum = 0 - nums[i]
                # [-4,-1,-1,0,1,2]
                while low < high:
                    print("i={} num[i] {} nums[low] {} nums[high] {} ".format(str(i), str(nums[i]), str(nums[low]),
                                                                              str(nums[high])))
                    if nums[low] + nums[high] == sum:
                        # print("i={} num[i] {} nums[low] {} nums[high] {} ".format(str(i),str(nums[i]),str(nums[low]),str(nums[high])))
                        outputList.append([nums[i],nums[low],nums[high]])
                        while low < high and nums[low] == nums[low+1]: low += 1
                        while low < high and nums[high] == nums[high-1]: high -= 1
                        low += 1
                        high -= 1
                    elif nums[low] + nums[high] > sum:
                        high -= 1
                    else:
                        low += 1
        return outputList

s = Solution()

ll = [-1,0,1,2,-1,-4]
print(s.threeSum(ll))
