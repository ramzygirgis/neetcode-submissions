class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hash initialization
        s_counts = {}
        t_counts = {}
        for s_char in s:
            s_counts[s_char] = 0;
        for t_char in t:
            t_counts[t_char] = 0;
        # counting
        for s_char in s:
            s_counts[s_char] += 1
        for t_char in t:
            t_counts[t_char] += 1
        # check for mismatch
        for s_char in s:
            if ((s_char not in t_counts.keys()) or (s_counts[s_char] != t_counts[s_char])):
                return False
        for t_char in t:
            if ((t_char not in s_counts.keys()) or (t_counts[t_char] != s_counts[t_char])):
                return False
        return True

            
            
        