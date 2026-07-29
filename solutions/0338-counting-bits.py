class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp
        # res = []
        # for num in range(n+1):
        #     one=0
        #     for i in range(32):
        #         if num &(1 << i):
        #             one+=1
        #     res.append(one)
        # return res

        