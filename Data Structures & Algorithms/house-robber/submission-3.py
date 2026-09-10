class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # we save the most amout of money in a list
        # at the same index as the current house

        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        
        return dp[n - 1]