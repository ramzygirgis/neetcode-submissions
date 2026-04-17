class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [1]
        suffix = [1]
        res = []
        left_prod = 1
        right_prod = 1
        for i in range(length - 1):
            left_prod *= nums[i]
            prefix.append(left_prod)
            right_prod *= nums[length - 1 - i]
            suffix.append(right_prod)
        for i in range(length):
            res.append(prefix[i] * suffix[length - 1 - i])
        return res