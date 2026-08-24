class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s) < len(t):
            return ""

        sDict = {}
        tDict = {}

        for char in t:
            tDict[char] = tDict.get(char,0) + 1 
                
        
        left = 0
        right = left
        have, need = 0, len(tDict)
        result = []
        resLen = float('infinity')
        while right < len(s):
            
            sDict[s[right]] =  sDict.get(s[right], 0) + 1

            if s[right] in tDict and sDict[s[right]] == tDict[s[right]]:
                have += 1

            while have == need:
                size = right - left + 1
                if size < resLen:
                    result = [left, right]
                    resLen = right - left + 1
                sDict[s[left]] -= 1
                
                    
                

                if s[left] in tDict and sDict[s[left]] < tDict[s[left]]:
                        have -= 1
                left += 1
                
            right += 1

        if not result:
            return ""
        else:
            return s[result[0]:result[1]+1]