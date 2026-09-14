class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_size = 0
        
        i = 0
        for j, char in enumerate(s):
            str_temp = s[i:j+1]
            
            if max_size < len(str_temp) and len(set(str_temp)) == len(str_temp):
                max_size += 1
            else:
                i+=1
        return max_size

