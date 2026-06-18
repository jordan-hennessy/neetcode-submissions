import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # e.g. piles=[1,4,3,2], h=6

        #                l  m     r
        # possible k -> [1, 2, 3, 4]

        left, right = 1, max(piles)
        # left=1, right=4

        while left <= right:
            k = (left + right) // 2  # k=2

            counter = 0 # = 6

            for i in range(len(piles)):
                counter += math.ceil(piles[i] / k)

            if counter <= h:  # k or lower
                right = k - 1
            else:
                left = k + 1

        return left

        # --- --- --- --- --- --- --- --- --- --- --- ---

        # Valid no. (k) is between (1 - max(piles))
        # Counter will count how many times a number goes into something.
        # If counter > h then right becomes k - 1
        # If counter <= h then left becomes k
        # When left <= right is not true then we have the answer??? -> k
