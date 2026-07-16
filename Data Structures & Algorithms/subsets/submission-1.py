class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []

        # We use DFS
        # Each number can either be `included` or `not`
        # 

        def dfs(i): 
            if i >= len(nums):          # We checked all branchs this side
                res.append(subset[:])
                return

            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res