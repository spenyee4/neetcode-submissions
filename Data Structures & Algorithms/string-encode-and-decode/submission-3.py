class Solution:

    def encode(self, strs: List[str]) -> str:
        #Use a value in front of each string
        encodedstring = ''
        for word in strs:
            length = len(word)
            encodedstring += str(length) + "#" + word
        return encodedstring

    def decode(self, s: str) -> List[str]:
        #Delimiter using the value in front of each string  
        result = []
        i = 0
        while i < len(s):
            j = i 
            while s[j] != '#':
                j += 1
            length = int(s[i:j]) # Get the value if bigger than one
            decodedlist = s[j + 1: j + 1 + length]
            result.append(decodedlist)
            i = j + 1 +length
        return result