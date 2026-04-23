class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        for num in nums:
            count[num] = count.get(num,0)+1

        sorted_nums = sorted(count,key=count.get,reverse=True)
        return sorted_nums[:k]


sol = Solution()
nums = [1,2,2,3,3,3]
k = 2
sol.topKFrequent(nums, k)