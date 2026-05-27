class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        test = set()
        for i in range(len(nums)):
            if nums[i] in test:
                return True
            else:
                test.add(nums[i])
        return False