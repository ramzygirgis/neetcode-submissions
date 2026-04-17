from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_set = set(nums)
        frequency = {}
        for number in num_set:
            frequency[number] = 0
        for number in nums:
            frequency[number] += 1
        counts = frequency.values()
        sorted_counts = sorted(counts, reverse = True)
        threshold = sorted_counts[k-1]
        L = []
        for number in nums:
            if frequency[number] >= threshold and number not in L:
                L.append(number)
        return L