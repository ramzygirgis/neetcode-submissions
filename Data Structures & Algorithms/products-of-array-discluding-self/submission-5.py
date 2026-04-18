class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L = [1]
        for i in range(n - 1):
            L.append(nums[i] * L[-1])
        R = [1]
        for i in range(n - 1):
            R.append(nums[n - 1 - i] * R[-1]) 
        res = []
        for i in range(n):
            res.append(L[i] * R[n - 1 - i])
        return res