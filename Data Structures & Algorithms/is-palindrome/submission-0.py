class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        #Can there be other values than characters such as integers and symbols?
        #Will there always be a valid input such as empty space
        #If it is jus an empty space, then would that be considered as a palindrome?
        newString = s.lower()
        print(newString)
        while left < right:
            if newString[left].isalnum() and newString[right].isalnum():
                if newString[left] == newString[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            elif not newString[left].isalnum():
                left += 1
            elif not newString[right].isalnum():
                right -= 1
        return True