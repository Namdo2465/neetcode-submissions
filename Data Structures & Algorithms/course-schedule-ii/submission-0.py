class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        Prereqs = defaultdict(list)
        for course, prereq in prerequisites:
            Prereqs[course].append(prereq)
        visited = set()
        ans = []
        def dfs(course):
            if course in visited:
                return False
            if Prereqs[course] == []:
                ans.append(course)
                return True
            visited.add(course)
            for prereq in Prereqs[course]:
                if not dfs(prereq):
                    return False
            ans.append(course)
            visited.remove(course)
            Prereqs[course] = []
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
        seen = set()
        res = []
        for num in ans:
            if num not in seen:
                res.append(num)
                seen.add(num)
        for num in range(numCourses):
            if num not in seen:
                res.append(num)
        return res
            
            