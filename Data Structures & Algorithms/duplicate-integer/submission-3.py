from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = defaultdict(int)
        for num in nums:
            if counts[num] > 0:
                return True
            counts[num] = 1
        return False