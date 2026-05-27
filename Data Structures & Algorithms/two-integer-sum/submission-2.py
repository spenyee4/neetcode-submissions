class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        result = []

        for i in range(len(nums)):
            value = target - nums[i]
            if value in seen:
                result = [seen[value],i]
            
            seen[nums[i]] = i
        
        return result