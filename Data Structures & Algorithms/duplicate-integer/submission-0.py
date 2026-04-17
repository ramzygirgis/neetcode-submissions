class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initialize counting hashmap
        count = {}
        for num in nums:
            count[num] = 0
        # now, count for duplicates
        for num in nums:
            if count[num] == 1:
                return True
            count[num] += 1
        return False