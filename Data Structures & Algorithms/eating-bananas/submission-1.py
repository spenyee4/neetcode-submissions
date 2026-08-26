import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        result = r

        while l <= r:
            mid = (l+r) // 2
            currTotal = 0
            for p in piles:
                currTotal += math.ceil(p / mid)
        
            if currTotal <= h:
                r = mid - 1
                result = mid
            else:
                l = mid + 1
            
        return result