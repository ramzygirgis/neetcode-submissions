class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triples = []
        nums = sorted(nums)
        length = len(nums)
        for i in range(length ):
            left = i + 1
            right = length - 1
            target = -nums[i]
            while left < right:
                curSum = nums[left] + nums[right]
                if curSum == target:
                    triple = [nums[i], nums[left], nums[right]]
                    if triple not in triples:
                        triples.append(triple)
                    left += 1
                if curSum > target:
                    right -= 1
                if curSum < target:
                    left += 1
        return triples