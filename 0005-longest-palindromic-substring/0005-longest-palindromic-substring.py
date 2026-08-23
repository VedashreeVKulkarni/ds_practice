class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        start = 0
        end = 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return left + 1, right - 1

        for i in range(len(s)):
            left, right = expand(i, i)
            current = right - left + 1
            if current > longest:
                longest = current
                start = left
                end = right

            left, right = expand(i, i + 1)
            current = right - left + 1
            if current > longest:
                longest = current
                start = left
                end = right

        return s[start:end + 1]