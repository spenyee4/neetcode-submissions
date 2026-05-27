class Solution:

    def encode(self, strs: List[str]) -> str:
        newString = ''
        for i in range(len(strs)):
            newString += str(len(strs[i])) + '#' + strs[i]
        
        return newString

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            result.append(s[j+1 : j+1+length])
            i = j + 1 + length

        print (result)
        return result