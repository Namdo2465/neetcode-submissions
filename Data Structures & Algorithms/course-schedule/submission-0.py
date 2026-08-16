class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        Prereqs = defaultdict(list)
        for course, prereq in prerequisites:
            Prereqs[course].append(prereq)
        visited_course = set()
        def dfs(course):
            if course in visited_course:
                return False
            if Prereqs[course] == []:
                return True
            visited_course.add(course)
            for prereq in Prereqs[course]:
                if not dfs(prereq):
                    return False
            visited_course.remove(course)
            Prereqs[course] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        