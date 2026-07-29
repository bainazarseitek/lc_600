class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.longestCommonSubseq(s, s[::-1])
    
    def longestCommonSubseq(self, s1, s2):
        l1, l2 = len(s1), len(s2)
        dp = [[0 for j in range(l1+1)] for i in range(l2+1)]
        for i in range(l1-1, -1, -1):
            for j in range(l2-1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = 1+ dp[i+1][j+1]
                else:
                     dp[i][j] =max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]

        