class Solution:
    def longestPalindrome(self, s: str) -> str:

        palindrome = s[0]
        index = 0

        while index < len(s):

            #even
            left = index
            right = index + 1
            current = ""

            while left >= 0 and right < len(s) and s[left] == s[right]:
                current = s[left] + current + s[right]

                if len(current) > len(palindrome):
                    palindrome = current

                left -= 1
                right += 1


            #odd
            left = index - 1
            right = index + 1
            current = s[index]

            while left >= 0 and right < len(s) and s[left] == s[right]:
                current = s[left] + current + s[right]

                if len(current) > len(palindrome):
                    palindrome = current
                left -= 1
                right += 1

            index += 1
        
        return palindrome
            


        