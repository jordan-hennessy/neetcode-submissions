class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        setnum = set(nums)

        res = 0
        
        for num in setnum:
            counter = 1

            while (num + counter) in setnum:
                counter += 1
            
            res = max(res, counter)
        
        return res