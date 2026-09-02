class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        LngStr = []
        maxLength = 0

        for i in range(len(s)):
            LngStr = []
            for j in s[i:]:
                if j not in LngStr:
                    LngStr.append(j)
                else:
                    break
            maxLength = max(maxLength, len(LngStr))

        return maxLength