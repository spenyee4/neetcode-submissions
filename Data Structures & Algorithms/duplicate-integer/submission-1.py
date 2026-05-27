class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        containsDuplicate = set()

        for index, num in enumerate(nums):
            if num not in containsDuplicate:
                containsDuplicate.add(num)
            else:
                return True
        return False