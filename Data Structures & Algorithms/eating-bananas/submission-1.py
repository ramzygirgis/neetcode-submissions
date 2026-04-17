from math import ceil
class Solution:
    def time(self, k, piles):
        totalTime = 0
        for pile in piles:
            totalTime += ceil(pile / k)
        return totalTime
         

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        curMin = r
        while l <= r:
            m = l + (r - l) // 2
            if self.time(m, piles) <= h:
                curMin = m
                r = m - 1
            else:
                l = m + 1
        return curMin