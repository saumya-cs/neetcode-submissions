class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0
        while left <= right:
            l = heights[left]
            r = heights[right]
            area = (right - left) * min(heights[left], heights[right])
            maxArea = max(maxArea, area)
            if l < r:
                left += 1
            else:
                right -= 1
        return maxArea
