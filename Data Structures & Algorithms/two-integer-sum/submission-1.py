class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        containSum = {}

        for index, val in enumerate(nums):
            temp = target - val
            if temp in containSum:
                return ([containSum[temp],index])
            else:
                containSum[val] = index