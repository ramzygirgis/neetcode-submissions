class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            count = [0] * 26 # a,b,c,...,z
            for c in s:
                count[ord(c)-ord('a')] += 1
            counts = tuple(count)
            if counts not in res.keys():
                res[tuple(count)] = [s]
            else:
                res[tuple(count)].append(s)
        L = []
        for key in res.keys():
            L.append(res[key])
        return L
        
                