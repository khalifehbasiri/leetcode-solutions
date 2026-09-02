class Solution:
    def reverseWords(self, s: str) -> str:
        reversedStr = s[::-1]
        words = []
        tempStr = ""

        for char in reversedStr:
            if char != " ":
                tempStr += char

            else:
                if tempStr != "":
                    words.append(tempStr[::-1])
                    tempStr = ""

        if tempStr != "":
            words.append(tempStr[::-1])
        
        return " ".join(words)
