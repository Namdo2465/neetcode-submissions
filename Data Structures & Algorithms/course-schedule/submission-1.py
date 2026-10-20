from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs_dict = defaultdict(list)
        for course, prereq in prerequisites:
            prereqs_dict[course].append(prereq)
        
        WHITE, GRAY, BLACK = 0, 1, 2
        # WHITE: not visited
        # GRAY: still in dfs path
        # BLACK: finished dfs(path)

        track = [WHITE] * numCourses
        # return True if there is a cycle, else False
        def check_cycle(course):
            if track[course] == BLACK:
                return False
            if track[course] == GRAY:
                return True
            track[course] = GRAY
            for prereq in prereqs_dict[course]:
                if check_cycle(prereq):
                    return True
            track[course] = BLACK
            return False
        
        for course in range(numCourses):
            if check_cycle(course):
                return False
        return True







        