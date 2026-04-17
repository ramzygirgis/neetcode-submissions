from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        count = defaultdict(int)
        l = 0
        r = 0
        max_len = 0
        count[s[0]] = 1
        while r < len(s) - 1: # our last pass will set r = len(s) - 1
            r += 1
            count[s[r]] += 1
            max_count = 0
            for c in count.keys():
                max_count = max(max_count, count[c])
            len_window = r - l + 1
            if len_window - max_count <= k:
                max_len = max(max_len, len_window)
            else:
                count[s[l]] -= 1
                l += 1
        return max_len
            