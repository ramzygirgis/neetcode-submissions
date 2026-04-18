class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        1-indexed, so return l + 1, r + 1
        """
        l = 0
        r = len(numbers) - 1
        while l < r:
            while numbers[r] + numbers[l] > target:
                r -= 1
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            l += 1
                
            
            
        