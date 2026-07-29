class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        subSet, curSet= [],[]
        self.helper(0, candidates, subSet, curSet, target)
        return subSet

    def helper(self, i,candidates, subSet, curSet, target):
        if target == 0:
            subSet.append(curSet.copy())
            return
        if i >=len(candidates) or target<0:
            return
        curSet.append(candidates[i])
        self.helper(i+1,candidates, subSet, curSet, target -candidates[i])
        curSet.pop()
        while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
            i+=1
        self.helper(i+1,candidates, subSet, curSet, target)

        