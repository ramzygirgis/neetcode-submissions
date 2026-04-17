class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_so_far = 0
        for i in range(len(nums)):
            if nums[i] - 1 in nums:
                continue
            length = 1
            while nums[i] + length in nums:
                length += 1
            if length > max_so_far:
                max_so_far = length
        return max_so_far
