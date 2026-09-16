class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount == 0:
            return 0

        best = float('inf')

        memo = [-1] * (amount + 1)

        memo[0] = 0     # base case

        def dfs(curr):      # curr is the amount we are checking rn

            if curr == 0:
                return 0

            if memo[curr] != -1:
                return memo[curr]   # the min amount of coins to get 'curr' amount

            best = float('inf')

            for i in range(len(coins)):
                if curr >= coins[i]:
                    best = min(best, 1 + dfs(curr - coins[i]))
            
            memo[curr] = best
            return memo[curr]
        
        dfs(amount)

        return memo[amount] if memo[amount] != float('inf') else -1