class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        string = ""
        for i in range(0,len(s)):
            if s[i].isalnum():
                string += s[i]
            else:
                pass
        for i in range(0,len(string)):
            if string[i] != string[len(string)-i -1]:
                return False
        return True

            
        