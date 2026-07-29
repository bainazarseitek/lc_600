class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        res= []
        for num in range(2**n):
            s=bin(num)[2:].zfill(n)
            if '11' not in s:
                cost=0
                for i, val in enumerate(s):
                    cost += i * int(val)
                if cost<=k:
                    res.append(str(s))
        return res
                    
            
        