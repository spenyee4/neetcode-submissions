class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        minStack = []
        for i in range(len(temperatures)):
            
            while minStack and temperatures[i] > minStack[-1][0]:
                
                
                result[minStack[-1][1]] = i - minStack[-1][1]
                minStack.pop()
            
            minStack.append((temperatures[i],i))
        
        return result


            
