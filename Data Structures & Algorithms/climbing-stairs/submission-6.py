class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
        if n == 2:
            return 2

        memo = {1: 1, 2: 2}

        def dp(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = dp(i - 2) + dp(i - 1)
                return memo[i] 

        return dp(n)
