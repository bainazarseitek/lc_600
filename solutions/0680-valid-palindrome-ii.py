class Solution:
    def validPalindrome(self, s: str) -> bool:

        # def isPalindrome(word):
        #     l,r = 0, len(word)-1
        #     while l < r:
        #         if word[l]==word[r]:
        #             l+=1
        #             r-=1
        #         else:
        #             return False
        #     return True

        l,r = 0, len(s)-1
        while l < r:
            if s[l]!=s[r]:
                skipL, skipR= s[l+1:r+1], s[l:r]
                return (skipL == skipL[::-1] or skipR == skipR[::-1])
            l+=1
            r-=1
        return True
            

            
        