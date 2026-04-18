class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set(nums) # small time optimization, memory cost
        max_so_far = 0
        for num in nums:
            if num - 1 in elements:
                continue
            r = 1
            while num + r in elements:
                r += 1
            max_so_far = max(max_so_far, r)
        return max_so_far
            
            