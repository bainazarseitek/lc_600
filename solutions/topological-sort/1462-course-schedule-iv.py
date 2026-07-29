class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        prereq = {i:[] for i in range(numCourses)}
        for pre, crs in prerequisites:
            prereq[crs].append(pre)
        prereqMap = {}
        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()
                for pre in prereq[crs]:
                    prereqMap[crs] |= dfs(pre)
                prereqMap[crs].add(crs)
            return prereqMap[crs]

        for crs in range(numCourses):
            dfs(crs)
        res = []
        for u, v in queries:
            res.append( u in prereqMap[v])
        return res        