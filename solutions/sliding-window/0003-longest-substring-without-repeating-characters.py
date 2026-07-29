class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        queue = deque()

        for R in range(len(s)):
            while s[R] in queue:
                queue.popleft()
            queue.append(s[R])               
            length = max(length,len(queue))
        return length   
            
            
            


        