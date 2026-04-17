class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums[0], nums[1])
        l = 0
        r = len(nums) - 1
        if nums[l] < nums[r]: # edge case; no shift
            return nums[0]

        while l <= r:
            m = l + (r-l)//2

            if m == len(nums) - 1: # if we reach the right, we can't access end index, but are surely at a min
                return nums[m]

            if nums[m - 1] >= nums[m] and nums[m + 1] >= nums[m]: # if we are at a loc min, we are a min
                return nums[m]
            if nums[m] < nums[l]:
                r = m - 1 # skip m
            else: #nums[l] < nums[m]
                if nums[l - 1] > nums[l]: # if min is at l
                    return nums[l] 
                l = m + 1# skip l
        return nums[m]