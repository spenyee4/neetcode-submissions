class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = left + 1
        seen = {}
        maxLength = 1
        #Add the first value
        if not s:
            return 0
        seen[s[left]] = left


        while right < len(s):
            if s[right] not in seen:
                seen[s[right]] = right
                length = right - left + 1
                maxLength = max(maxLength, length)
                right += 1
            else:
                if seen[s[right]] < left:
                    seen[s[right]] = right
                    length = right - left + 1
                    maxLength = max(maxLength, length)
                    right += 1
                    
                else:
                    left = seen[s[right]] + 1
                    seen[s[right]] =  right
                    right += 1
        return maxLength