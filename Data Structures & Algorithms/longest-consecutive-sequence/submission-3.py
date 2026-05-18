class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        setNums = set(nums)

        res = 0

        for num in setNums:
            counter = 1

            while (num + counter) in setNums:
                counter += 1

            res = max(res, counter)
        
        return res
            