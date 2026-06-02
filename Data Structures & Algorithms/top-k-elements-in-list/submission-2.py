class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #count the values of each char in a dict
        #create a list that holds the repeated char in that amount
        #go down from the list 
        countNums = {}

        for num in nums:
            if num not in countNums:
                countNums[num] = 1
            else:
                countNums[num] += 1
        
        #Create an empty array of 0s

        length = len(nums) + 1
        countList = []

        for _ in range(length):
            countList.append([])
        
        #print (countList)

        for keys, vals in countNums.items():
            countList[vals].append(keys)
        
        #print (countList)
        result = []

        for i in range(len(nums), -1, -1):
            for j in range(len(countList[i])):
                result.append(countList[i][j])
                if len(result) == k:
                    return result
                



        #return result

                
                