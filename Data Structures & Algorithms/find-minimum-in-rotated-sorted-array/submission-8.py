class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # still do regular binary but with an extra check

        #########
        # nums = [3,4,5,|6,1,2]

        # left = 3 (0), right = 2 (5), mid = 5 (2)
        # left = 6 (3), right = 2 (5), mid = 1 (4)

        # left = 6 (3), right = 1 (4), mid = 6 (3)

        # left = 1 (4), right = 1 (4), mid = x (x)

        #########

        left = 0
        right = len(nums) - 1

        # since mid still could be correct
        # we use left < right

        # we are looking for a case where a number is smaller than
        # the number before it

        while left < right:
            mid = (right + left) // 2

            # Smallest is on the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid

        return nums[right]

            
