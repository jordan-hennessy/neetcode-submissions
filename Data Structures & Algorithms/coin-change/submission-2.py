class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # I know it is like a tree

        if amount == 0:
            return 0

        best = float('inf')

        # we want to always find the least amount of coins to reach an 'amount'
        # base case -> amount = 0 -> coins = 0

        memo = [-1] * (amount + 1)
        memo[0] = 0

        # amount = 5
        # memo = [0,-1,-1,-1,-1,-1]
        #         0, 1, 2, 3, 4, 5  

        # curr -> the amount we have to calculate
        # e.g. to get 5 we have to get 4 -> 3 -> 2 -> 1 -> 0

        # wait are we tracking num coins or the amount left
        # memo is the num of coins

        # lets try get the min for a single coin at each 'amount' first

        def dfs(curr):
            if curr == 0:
                return 0
            
            if memo[curr] != -1:
                return memo[curr]

            best = float('inf')
            for i in range(len(coins)):
                if curr >= coins[i]:
                    best = min(1 + dfs(curr - coins[i]), best)
                
            memo[curr] = best


            return best

        dfs(amount)

        return memo[amount] if memo[amount] != float('inf') else -1