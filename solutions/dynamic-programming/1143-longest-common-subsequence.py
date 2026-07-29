class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # #TRUE dp
        # dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        # for i in range(len(text1)-1, -1, -1):
        #     for j in range(len(text2)-1, -1, -1):
        #         if text1[i] == text2[j]:
        #             dp[i][j] = 1+dp[i+1][j+1]
        #         else:
        #             dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        # return dp[0][0]
        

        # # dfs
        # s1,s2 = text1, text2
        # def dfs(i1, i2):
        #     if i1==len(s1) or i2==len(s2):
        #         return 0
        #     if s1[i1] == s2[i2]:
        #         return 1+ dfs(i1+1, i2+1)
        #     else:
        #         return max(dfs(i1+1, i2), dfs(i1, i2+1))
        # return dfs(0,0)

        #memoization
        s1,s2 = text1, text2
        cache = [[-1 for j in range(len(s2))] for i in range(len(s1))]
        def dfs(i, j, cache):
            if i==len(s1) or j==len(s2):
                return 0
            if cache[i][j] != -1:
                return cache[i][j]
            if s1[i] == s2[j]:
                cache[i][j] = 1+ dfs(i+1, j+1, cache)
            else:
                cache[i][j] = max(dfs(i+1, j, cache), dfs(i, j+1, cache))
            return cache[i][j]
        return dfs(0,0, cache)