class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            compareNumber = numbers[left] + numbers[right]
            if compareNumber > target:
                right -= 1
            elif compareNumber < target:
                left += 1
            else:
                return([left+1,right+1])
            
            
