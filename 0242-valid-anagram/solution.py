class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        charS = {}
        charT = {}

        for char in s:
            charS[char] = charS[char] + 1 if char in charS else 1
    
        for char in t:
            charT[char] = charT[char] + 1 if char in charT else 1
        
        return charS == charT