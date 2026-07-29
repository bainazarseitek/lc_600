class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd, mx = [], 0
        for n in nums:
            mx=max(mx, n)
            prefixGcd.append(gcd(n, mx))
        prefixGcd.sort()
        
        total = 0
        l, r = 0, len(prefixGcd)-1
        while l < r:
            total += gcd(prefixGcd[l], prefixGcd[r])
            l=l+1
            r=r-1
        return total
        