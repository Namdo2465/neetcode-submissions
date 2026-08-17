class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        Connections = defaultdict(list)
        for node, neighbour in edges:
            Connections[node].append(neighbour)
            Connections[neighbour].append(node)
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for neighbour in Connections[node]:
                if neighbour == parent:
                    continue
                if not dfs(neighbour, node):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n
                