class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anag = {}

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1
            
            key = tuple(count)
            if key not in anag:
                anag[key] = []
            anag[key].append(word)

        return list(anag.values())