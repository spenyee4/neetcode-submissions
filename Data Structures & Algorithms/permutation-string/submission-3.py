class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Dict = {}
        s2Dict = {}
        
        left = 0
        right = left
        s1Length = len(s1)

        if len(s2) < len(s1):
            return False

        for char in s1:
            if char not in s1Dict:
                s1Dict[char] = 1
            else:
                s1Dict[char] += 1
       

        while right < len(s2):
            s2Dict[s2[right]] = s2Dict.get(s2[right], 0) + 1
            if right - left + 1 == s1Length:
                print(f"s1 {s1Dict}")
                print(f"s2 {s2Dict}")
                if s1Dict == s2Dict:
                    return True
                else:
                    s2Dict[s2[left]] = s2Dict.get(s2[left], 0) - 1
                    if s2Dict[s2[left]] == 0:
                        s2Dict.pop(s2[left])
                    left += 1
                    right += 1
                    
            else:
                right += 1
                         
        return False