class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_so_far = 0
        for n in num_set:
            if n - 1 not in num_set:
                index = 0
                while n + index + 1 in num_set:
                    index += 1
                length = index + 1
                if length > max_so_far:
                    max_so_far = length
        return max_so_far
