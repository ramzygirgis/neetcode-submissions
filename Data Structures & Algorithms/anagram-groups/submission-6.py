class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = {}
        for s in strs:
            L = [0] * 26
            for c in s: # O(nm), where m is maxstringsize
                L[ord(c) - ord('a')] += 1
            counts[s] = L.copy()
        inverse = {}
        for s in strs:
            key = tuple(counts[s])
            inverse.setdefault(key, []).append(s)
        return list(inverse.values())
            
            