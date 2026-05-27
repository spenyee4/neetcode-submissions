class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        table = {}

        for i in range(len(nums)):
            if nums[i] in table:
                return ([table[nums[i]],i])
            missingPair = target - nums[i]
            table[missingPair] = i
            
