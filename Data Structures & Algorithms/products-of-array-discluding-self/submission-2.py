class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left_prods = [1] * length
        right_prods = [1] * length
        for i in range(0, len(nums) - 1):
            left_prods[i + 1] = nums[i] * left_prods[i]
            right_prods[i + 1] = nums[length - 1 - i] * right_prods[i]
        print(right_prods)
        print(left_prods)
        res = []
        for i in range(0, len(nums)):
            res.append(left_prods[i] * right_prods[ length - i -1])
        return res