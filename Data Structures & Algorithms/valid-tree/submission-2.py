from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        connections = defaultdict(list)
        for node1, node2 in edges:
            connections[node1].append(node2)
            connections[node2].append(node1)
        
        visited = set()
        def dfs(node, parent):
            visited.add(node)
            for nei in connections[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                if not dfs(nei, node):
                    return False
            return True
        
        if not dfs(0, -1):
            return False
        return len(visited) == n
