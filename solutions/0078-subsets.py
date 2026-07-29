class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subSet = []
        res = []
        def dfs(i):
            if i>=len(nums):
                res.append(subSet.copy())
                return
            #include 
            subSet.append(nums[i])
            dfs(i+1)

            #not include
            subSet.pop()
            dfs(i+1)

        dfs(0)
        return res