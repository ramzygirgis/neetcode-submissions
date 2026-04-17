class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        onLeft = nums[l] <= target
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            if onLeft:
                if nums[m] < target and nums[m] >= nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[m] < target or nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1






        # while l <= r:
        #     m = l + (r - l)// 2
        #     print(f'l: {l}, m: {m}, r: {r}')
        #     if nums[m] == target:
        #         return m
        #     if nums[m] < target and nums[m] > nums[r]:
        #         l = m + 1
        #     elif onLeft and nums[m] < target and nums[m] <= nums[r]:
        #         r = m - 1
        #     elif onRight and nums[m] > nums[r]:
        #         l = m +1
        #     else:
        #         r = m - 1
        return -1
            
                    
                    
