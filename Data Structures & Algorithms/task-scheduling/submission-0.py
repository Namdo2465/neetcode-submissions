class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        count.sort()
        maxTask = count[25]
        idle = (maxTask - 1) * n
        for i in range(25):
            idle -=min(maxTask - 1, count[i]) 
        return max(0, idle) + len(tasks)

        