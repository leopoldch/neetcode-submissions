from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        prerequisitesMap = defaultdict(list)

        for course, prereq in prerequisites:
            prerequisitesMap[course].append(prereq)
        

        # we want to detect cycles

        validated = [0]*numCourses

        def hasCycle(course):
            
            if validated[course] == 1:
                return True
            
            if validated[course] == 2:
                return False
            
            validated[course] = 1 

            for prereq in prerequisitesMap[course]:
                if hasCycle(prereq):
                    return True

            validated[course] = 2

            return False


        for course in range(numCourses):
            if hasCycle(course):
                return False
        
        return True


