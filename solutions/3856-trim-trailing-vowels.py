class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vowels=set("aeiou")
        i = len(s)-1
        while s[i] in vowels and i>=0:
            i-=1
        return s[:i+1]
        
        