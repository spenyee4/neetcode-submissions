class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        isAnagram = defaultdict(list)

        for word in strs:
            newWord = sorted(word)
            anagram = ''.join(newWord)
            isAnagram[anagram].append(word)
        
        result = []

        for value in isAnagram.values():
            result.append(value)
        return result