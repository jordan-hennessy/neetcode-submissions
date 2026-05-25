class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        currentMax = 0

        for i in range(n):

            for j in range(i + 1, n):
                multiplier = j - i
                lower = min(heights[i], heights[j])

                val = multiplier * lower

                currentMax = max(currentMax, val)

        return currentMax
