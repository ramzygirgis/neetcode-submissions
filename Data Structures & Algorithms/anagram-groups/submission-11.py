from collections import defaultdict

class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     """
    #     return True if s and t are anagrams, false otherwise
    #     """
    #     if len(s) != len(t):
    #         return False
    #     counts = defaultdict(int)
    #     for c in s:
    #         counts[c] += 1
    #     for c in t:
    #         if counts[c] == 0:
    #             return False
    #         counts[c] -= 1
    #     return True


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        equiv_classes = defaultdict(list)
        for s in strs:
            # can also check if anagram in O(n)
            key = ''.join(sorted(s))
            equiv_classes[key].append(s)
        return list(equiv_classes.values())
