class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        Connections = defaultdict(list)
        for node, neighbour in edges:
            Connections[node].append(neighbour)
            Connections[neighbour].append(node)
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbour in Connections[node]:
                if neighbour not in visited:
                    dfs(neighbour)
        cnt = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                cnt += 1
        return cnt