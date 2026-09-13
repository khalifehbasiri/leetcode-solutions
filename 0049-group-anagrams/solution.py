class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = {}

        for char in strs:
            key = "".join(sorted(char))

            if key not in temp:
                temp[key] = []

            temp[key].append(char)

        return list(temp.values())