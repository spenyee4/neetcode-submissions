class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countAnagramS = {}
        countAnagramT = {}

        for char in s:
            if char not in countAnagramS:
                countAnagramS[char] = 0
            else:
                countAnagramS[char] += 1
        for char in t:
            if char not in countAnagramT:
                countAnagramT[char] = 0
            else:
                countAnagramT[char] += 1
        
        if countAnagramS == countAnagramT:
            return True
        else:
            return False