class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = set(nums)
        maxCount = 1
        newCount = 0
        if not nums:
            return 0

        for num in count:
            if num -1 not in count:
                newCount = 1
                while num + newCount in count:
                    newCount += 1
                    maxCount = max(maxCount, newCount)
        
        return maxCount
