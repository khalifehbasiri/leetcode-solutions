class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #two pointer both starting at the front, left only moves when we find a duplicate, and it keeps moving till it doesnt have any duplicates

        ourSet = set()
        maxLength = 0
        currLen = 0

        left = 0
        for right in range(len(s)):
    
            while s[right] in ourSet:
                ourSet.remove(s[left])
                currLen -= 1
                left += 1

            ourSet.add(s[right])
            currLen += 1

            maxLength = max(maxLength, currLen)
        
        return maxLength




