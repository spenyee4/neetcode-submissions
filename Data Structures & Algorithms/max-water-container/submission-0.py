class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxWater = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            distance = right - left
            if heights[left] > heights[right]:
                currWater = distance * heights[right]
                maxWater = max(maxWater, currWater)
                right -= 1

            elif heights[left] < heights[right]:
                currWater = distance * heights[left]
                maxWater = max(maxWater, currWater)
                left += 1
            else:
                currWater = distance * heights[left]
                maxWater = max(maxWater, currWater)
                left += 1
                right -= 1
            
        return maxWater