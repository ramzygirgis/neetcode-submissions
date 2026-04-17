class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        l = 0
        r = 1
        maxSoFar = 0
        while r < len(s):
            if s[r] in s[l:r]:
                maxSoFar = max(maxSoFar, r - l)
                l += 1
            else:
                if r == len(s) - 1:
                    maxSoFar = max(maxSoFar, r - l + 1)
                    break
                r += 1
        return maxSoFar
        