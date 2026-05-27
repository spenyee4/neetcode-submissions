class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sTable = {}
        tTable = {}
        for char in s:
            if char in sTable:
                sTable[char] += 1
            else:
                sTable[char] = 0
        
        for char in t:
            if char in tTable:
                tTable[char] += 1
            else:
                tTable[char] = 0
        
        if sTable == tTable:
            return True
        return False
