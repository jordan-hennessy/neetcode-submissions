class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        res = 0

        numset = set(nums)

        for num in numset:
            counter = 1
            while (num + counter) in numset:
                counter += 1
            
            res = max(res, counter)
        
        return res