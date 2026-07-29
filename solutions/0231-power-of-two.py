class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and (n & (n - 1)) == 0

        # x= 1
        # while x < n:
        #     x *=2
        # return x == n







        # if n == 1:
        #     return True
        # x = n/2
        # while x != 1:
        #     if x % 2 == 0:
        #         x = x/2
        #     else:
        #         return False
        # return True