class Solution:
    def trap(self, height: List[int]) -> int:

        res = 0
        # n -> last index
        n = len(height) - 1

        # No water in height[0] or height[n]
        for i in range(1, n):
            l, r = i - 1, i + 1

            leftMax, rightMax = 0, 0

            while l >= 0:
                leftMax = max(leftMax, height[l])
                l -= 1

            while r <= n:
                rightMax = max(rightMax, height[r])
                r += 1

                val = min(leftMax, rightMax) - height[i]

            if val > 0:
                res += val

        return res
