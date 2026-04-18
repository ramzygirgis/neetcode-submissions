class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_so_far = 0
        for num in nums:
            if num - 1 in nums:
                continue
            r = 1
            while num + r in nums:
                r += 1
            max_so_far = max(max_so_far, r)
        return max_so_far
            
            