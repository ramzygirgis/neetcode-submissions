class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) - 1
        curMax = 0
        while l < r:
            if heights[l] < heights[r]:
                curMax = max(heights[l]* (r - l), curMax)
                l += 1
            else:
                curMax = max(heights[r]* (r - l), curMax)
                r -= 1
        return curMax