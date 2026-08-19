class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxLength = 0

        for val in seen:
            if val - 1 not in seen:
                length = 1
                curr = val
                while curr + 1 in seen:
                    curr += 1
                    length += 1
                maxLength = max(length,maxLength)
        
        if len(nums):
            return maxLength
        else:
            return 0

                
