from collections import defaultdict

class Solution:
    def getKey(self, s: str):
        counts = [0] * 26
        for c in s:
            counts[ord(c) - ord('a')] += 1
        return tuple(counts)

    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    #     equiv_classes = defaultdict(list)
    #     for s in strs:
    #         frequencies = s
    #     return list(equiv_classes.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        equiv_classes = defaultdict(list)
        for s in strs:
            equiv_classes[self.getKey(s)].append(s)
        return list(equiv_classes.values())