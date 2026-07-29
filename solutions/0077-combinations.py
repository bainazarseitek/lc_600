class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb, curComb = [], []
        self.helper(1, n,k,comb, curComb)
        return comb

    def helper(self, i, n, k, comb, curComb):
        if len(curComb) == k:
            comb.append(curComb.copy())
            return
        if i > n:
            return
        for j in range(i, n+1):
            curComb.append(j)
            self.helper(j+1, n,k,comb, curComb)
            curComb.pop()


        ## same as subsets(add or not add):
        # curSet.append(i)
        # self.helper(i+1, curSet, comb,n,k)
        # curSet.pop()

        # self.helper(i+1, curSet, comb,n,k)
