class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        subSet, curSet = [],[]
        self.helper(0, candidates, subSet, curSet, target)
        return subSet

    def helper(self, i, candidates, subSet, curSet, target):
        if target == 0:
            subSet.append(curSet.copy())
            return
        if i >= len(candidates) or target < 0:
            return
        
        curSet.append(candidates[i])
        self.helper(i, candidates, subSet, curSet, target-candidates[i])
        curSet.pop()

        self.helper(i+1, candidates, subSet, curSet, target)

        