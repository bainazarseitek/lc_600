class Solution:
    def is_contained(self, map1, map2):
        for char, count in map1.items():
            if map2.get(char,0)<count:
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        thash={}
        for ch in t:
            thash[ch]=thash.get(ch,0)+1
        l,r=0,0
        cur={}
        window=""
        best_len=float("inf")
        while r<len(s):
            cur[s[r]]=cur.get(s[r],0)+1
            while self.is_contained(thash,cur):
                temp_window=s[l:r+1]
                if best_len>len(temp_window):
                    window=temp_window
                    best_len=len(temp_window)
                left_char=s[l]                   
                cur[left_char]-=1
                if cur[s[l]]==0:
                    del cur[s[l]]
                l+=1
            r+=1
        return window
            

        
        
        