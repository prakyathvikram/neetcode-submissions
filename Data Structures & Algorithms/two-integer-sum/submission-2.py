class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return[seen[complement], i]
            seen[num] = i
        
sol = Solution()
nums = [3,4,5,6]
target = 7
sol.twoSum(nums,target)
