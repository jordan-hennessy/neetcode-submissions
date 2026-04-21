class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)

        res = 0
        
        for num in numSet:

            counter = 1

            while (num + counter) in numSet:
                counter += 1
            res = max(res, counter)
        
        return res
