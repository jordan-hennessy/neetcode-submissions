class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        numSet = set(nums)

        if len(nums) == len(numSet):
            return False
        
        return True