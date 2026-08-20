class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for index, value in enumerate(numbers):
            newTarget = target - value
            if newTarget in seen:
                return ([seen[newTarget]+1, index+1])
            else:
                seen[value] = index
        