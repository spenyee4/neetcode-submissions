class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seenWords = defaultdict(list)

        for word in strs:
            sortWord = sorted(word)
            sortedWord = ''.join(sortWord)
            seenWords[sortedWord].append(word)
            
        
        result = []

        for keys in seenWords:
            result.append(list(seenWords[keys]))
        return result