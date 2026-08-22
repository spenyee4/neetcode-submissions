class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longestSub = {}

        left = 0
        maxSub = 0
        result = 0

        for right in range(len(s)):
            # Add current character to the window
            longestSub[s[right]] = longestSub.get(s[right], 0) + 1

            # Track the most frequent character
            maxSub = max(maxSub, longestSub[s[right]])

            # Current window size
            size = right - left + 1

            # Number of replacements needed
            while size - maxSub > k:
                longestSub[s[left]] -= 1
                left += 1
                size = right - left + 1

            # Valid window
            result = max(result, size)

        return result