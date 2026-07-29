class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, curSub= [],[]
        self.helper(0, s, res, curSub)
        return res

    def helper(self,i, s, res, curSub):
        if i == len(s):
            res.append(curSub.copy())
            return
        for j in range(i, len(s)):
            if self.isPalindrome(s, i, j):
                curSub.append(s[i:j+1])
                self.helper(j+1,s,res,curSub)
                curSub.pop()
        
    def isPalindrome(self, s,l,r):
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
        