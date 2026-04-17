class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_zeros = 0
        length = len(nums)
        res = length * [0]
        prod = 1
        for i in range(length):
            if nums[i] == 0:
                num_zeros += 1
                index = i
            else:
                prod *= nums[i]
        if num_zeros > 1:
            return res
        if num_zeros == 1:
            res[index] = prod
            return res
        res = [prod] * length
        for i in range(length):
            res[i] = res[i] // nums[i]
        return res
            

            