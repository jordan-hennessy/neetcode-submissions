class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1

        # Find pivot first

        while left < right:

            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        pivot = left

        left, right = 0, pivot

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        left, right = pivot, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1


                