class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        res = 0

        # e.g. heights = [1,7,2,5,4,7,3,6]
        l, r = 0, len(heights) - 1
        # l = 0, r = 7

        while l < r:    # not '<='
            curr = min(heights[l], heights[r]) * (r - l)
            res = max(curr, res)

            # hmmmmmm, what do I move???
            # maybe move the smaller height?

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return res

