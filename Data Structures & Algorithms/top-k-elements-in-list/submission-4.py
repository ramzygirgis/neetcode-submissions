class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        length = len(nums)
        
        res = []
        for i in range(len(freq) - 1, 0 , -1):
            for i in freq[i]:
                res.append(i)
            if len(res) == k:
                return res