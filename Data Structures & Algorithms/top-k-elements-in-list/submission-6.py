from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_count = 0
        counts = defaultdict(int)
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            max_count = max(max_count, counts[num])
        counts_inv = defaultdict(list)
        for num in counts.keys():
            counts_inv[counts[num]].append(num)
        cur = len(nums)
        accum = 0
        res = []
        while accum < k:
            res.extend(counts_inv[cur])
            accum += len(counts_inv[cur])
            cur -= 1

        return res