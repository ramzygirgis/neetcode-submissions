class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        inverse = {}
        numset = set(nums)
        for n in numset:
            inverse.setdefault(counts[n], []).append(n)
        res = []
        
        m = 0
        for i in range(len(nums), 0, -1):
            if m >=k:
                break
            if i in inverse.keys():
                res += inverse[i]
                m += len(inverse[i])
        return res
            
            
