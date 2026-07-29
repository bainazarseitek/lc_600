class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1hash={}
        for s in s1:
            s1hash[s]=s1hash.get(s, 0)+1
        
        l, r = 0, len(s1)
        s2hash={}
        for s in s2[l:r]:
            s2hash[s]=s2hash.get(s, 0)+1

        while r < len(s2):
            if s1hash == s2hash:
                return True
            
            left_char=s2[l]
            s2hash[left_char]-=1
            if s2hash[left_char]==0:
                del s2hash[left_char]
            right_char=s2[r]
            s2hash[right_char] = s2hash.get(right_char, 0) + 1



            l+=1
            r+=1
        return s1hash == s2hash


        