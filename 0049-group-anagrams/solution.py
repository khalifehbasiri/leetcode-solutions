class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anag = {}

        for i, x in enumerate(strs):
            sorted_x = "".join(sorted(x))

            if sorted_x not in anag:
                anag[sorted_x] = []
            anag[sorted_x].append(x)
        
        final = []
        for x in anag.values():
            final.append(x)
        
        return final
