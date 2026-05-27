class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        numCount = []
        for i in range(len(nums)):
            numCount.append([])
        
        
        for keys,values in count.items():
            numCount[values-1].append(keys)

        result = []
        matchK = 0
        for i in range(len(nums)-1,-1,-1):
            print(numCount[i])
            if numCount[i] and matchK < k:
                for j in numCount[i]:
                    result.append(j)
                    matchK += 1
        print(result)
        return result