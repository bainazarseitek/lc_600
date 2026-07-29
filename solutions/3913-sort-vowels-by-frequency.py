class Solution:
    def sortVowels(self, s: str) -> str:
        vowels=['a','e','i','o','u']
        first_pos={}
        freq=defaultdict(int)
        for i,l in enumerate(s):
            if l in vowels:
                freq[l]+=1
                if l not in first_pos:
                    first_pos[l]=i
        heap=[]
        for vowel, count in freq.items():
            heappush(heap, (-count,first_pos[vowel], vowel))
        sorted_v=[]
        while heap:
            count,first_inx, val=heappop(heap)
            sorted_v.extend([val]*(-count))
        res=""
        idx=0
        for l in s:
            if l not in vowels:
                res+=l
            else:
                res += sorted_v[idx]
                idx+=1
        return res
                
        