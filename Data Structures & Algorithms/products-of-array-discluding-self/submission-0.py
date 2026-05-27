class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1,1,2,8]
        #[48,24,6,1]

        leftArray = [1] * len(nums)
        rightArray = [1] * len(nums)
        for i in range(1,len(nums)):
            leftArray[i] = leftArray[i-1] * nums[i-1]
       

        for j in range(len(nums)-2,-1,-1):
            rightArray[j] = rightArray[j+1] * nums[j+1]
        
        result = [1] * len(nums)
        for k in range(len(leftArray)):
            result[k] = leftArray[k] * rightArray[k]
        
        return result