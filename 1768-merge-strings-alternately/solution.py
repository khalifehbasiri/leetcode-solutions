class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        maxLen = max(len(word1), len(word2))
        newStr = ""
        i = 0
        while i < maxLen:
            if i < len(word1):
                newStr += word1[i]
            if i < len(word2):
                newStr += word2[i]
            i += 1
        return newStr

            