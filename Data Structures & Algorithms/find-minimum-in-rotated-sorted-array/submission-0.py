class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                result = nums[left]

            middle = (left + right) // 2

            if nums[middle] > nums[right]:
                left = middle + 1
            elif nums[middle] < nums[left]:
                right = middle 
            else:
                
                return nums[left]