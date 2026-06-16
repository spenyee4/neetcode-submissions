class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        #[1,2,4,6]
        #[1,1,2,8]
        #[48,24,6,1]

        array1 = [1] * len(nums)
        array2 = [1] * len(nums)
        result = [1] * len(nums)

        for i in range(1,len(nums),1):
            array1[i] = nums[i-1] * array1[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            array2[i] = nums[i+1] * array2[i+1]
        
        for i in range(len(array1)):
            result[i] = array1[i] * array2[i]
        
        return result
        #[6,4,2,1]
        #[1,2,8,48]
        #[]