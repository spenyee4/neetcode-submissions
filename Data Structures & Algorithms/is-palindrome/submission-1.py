class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        newString = s.lower()
        
        while left < right:
            

            
            if not newString[left].isalnum():
                left += 1 
            elif not newString[right].isalnum():
                right -= 1
            elif newString[left].isalnum() and newString[right].isalnum() and newString[left] != newString[right]:
                return False
            else:
                left += 1
                right -= 1
        return True