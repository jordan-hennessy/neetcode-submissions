class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = set()

        # nums = [-4, -1, -1, 0, 1, 2]

        for i in range(len(nums)):

            left = i + 1            # i = 0 -> -4, left = 1 -> -1
            right = len(nums) - 1   # right = 5 -> 2

            while left < right:
                
                val = nums[i] + nums[left] + nums[right]

                if val == 0:
                    res.add((nums[i], nums[left], nums[right]))

                if val < 0:
                    left += 1
                else:
                    right -= 1
                
        return list(res)