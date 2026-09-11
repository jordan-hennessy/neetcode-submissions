class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # a valid tree has len(edges) == n - 1
        # this is a fact
        if len(edges) > n - 1:
            return False

        nodes = n

        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visit = set()

        def dfs(node):
            visit.add(node)
            for nei in adj[node]:
                if nei in visit:
                    continue
                dfs(nei)
            return 
        
        dfs(0)

        return len(visit) == n