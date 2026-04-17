class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if len(s1) == 0:
            return True

        l = 0
        counts = {}
        for c in s1:
            counts[c] = counts.get(c, 0) + 1
        
        while l < len(s2):
            if s2[l] not in counts.keys():
                l += 1
                continue
            r = l
            while r < len(s2):
                if s2[r] not in counts.keys():
                    for i in range(l, r):
                        counts[s2[i]] += 1
                    break
                counts[s2[r]] -= 1
                if r - l + 1 == len(s1):
                    if max(counts.values()) <= 0:
                        return True
                    if r + 1 == len(s2) or s2[r + 1] not in counts.keys():
                        for i in range(l, r + 1):
                            counts[s2[i]] += 1
                        break
                     #counts[s2[r + 1]] -= 1 
                    counts[s2[l]] += 1
                    print(counts.values())
                    l += 1
                r += 1
                
            l = r + 1
        return False
            
        
