from collections import deque
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    
        left = 0
        right = 0

        heap = []
        result = []

        while right < len(nums):

            size = right - left + 1
            heapq.heappush(heap, (nums[right] * -1, right))

            if size == k:
                
                while left > heap[0][1]: #Outside of the window
                    heapq.heappop(heap)
                result.append(heap[0][0]*-1)
                left += 1
            right += 1
        return result