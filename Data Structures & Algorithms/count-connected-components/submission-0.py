class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        num_comp = 0

        adj = defaultdict(list)

        visit = set()

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        
        def dfs(node):
            visit.add(node)

            for nei in adj[node]:
                if nei in visit:
                    continue
                dfs(nei)
            return

        # we could loop through each node.
        # if we are discovering new nodes then we count one comp
        # if we are counting the same nodes then we dont count comp

        for i in range(n):
            if i in visit:
                continue
            else:
                num_comp += 1
                dfs(i)
            
        return num_comp