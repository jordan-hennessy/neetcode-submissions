class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        num_comp = 0

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

        for i in range(n):
            if i in visit:
                continue
            else:
                num_comp += 1
                dfs(i)
            
        return num_comp
