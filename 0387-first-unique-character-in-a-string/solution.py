class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_rep = {}


        for char in s:
            if char in char_rep:
                char_rep[char] += 1
            else:
                char_rep[char] = 1

        for i, char in enumerate(s):
            if char_rep[char] == 1:
                return i
        
        return -1