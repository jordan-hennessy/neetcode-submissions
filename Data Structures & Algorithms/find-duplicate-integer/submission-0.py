class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        if not nums:
            return None

        seen = set()

        for i in range(len(nums)):

            if nums[i] in seen:
                return nums[i]
            else:
                seen.add(nums[i])

        return -1

