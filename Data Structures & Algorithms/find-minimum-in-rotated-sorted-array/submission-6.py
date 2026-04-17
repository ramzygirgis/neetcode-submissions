class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums[0], nums[1])
        l = 0
        r = len(nums) - 1
        if nums[l] < nums[r]:
            return nums[0]

        while l <= r:
            m = l + (r-l)//2
            print(f'l: {l}, m: {m}, r: {r}')
            if m == len(nums) - 1:
                return nums[m]
            if nums[m - 1] >= nums[m] and nums[m + 1] >= nums[m]:
                return nums[m]
            if nums[m] < nums[l]:
                r = m - 1
            else: #nums[l] < nums[m]
                if nums[l - 1] > nums[l]:
                    return nums[l]
                l = m + 1
        return nums[m]