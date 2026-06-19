import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left, right = 1, max(piles)

        while left < right:

            k = (left + right) // 2

            count = 0

            for i in range(len(piles)):
                count += math.ceil(piles[i] / k)
            
            if count > h: # if count is too much (invalid)
                left = k + 1
            else:
                right = k
        
        return left

        # --- --- --- --- --- --- --- --- --- --- --- ---

        # Valid no. (k) is between (1 - max(piles))
        # Counter will count how many times a number goes into something.
        # If counter > h then right becomes k
        # If counter <= h then left becomes k + 1
        # When left <= right is not true then we have the answer??? -> k
