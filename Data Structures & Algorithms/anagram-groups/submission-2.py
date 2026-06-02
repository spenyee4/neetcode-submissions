from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Sort each word by char and hold in dict
        sortedString = defaultdict(list)

        for word in strs:
            sortedWord = ''.join(sorted(word))
   
            if sortedWord not in sortedString:
                sortedString[sortedWord].append(word)
            else:
                sortedString[sortedWord].append(word)

        return list(sortedString.values())