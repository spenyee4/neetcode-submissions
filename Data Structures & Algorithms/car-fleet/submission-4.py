class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        zipped = list(zip(position,speed))
        zipped.sort(reverse=True)
        stack = []

        fleet= 0
        for pos, spe in zipped:
            time = (target-pos) / spe
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        return len(stack)   