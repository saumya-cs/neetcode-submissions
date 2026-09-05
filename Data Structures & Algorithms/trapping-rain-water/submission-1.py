class Solution:
    def trap(self, height: List[int]) -> int:
        #is there a taller bar to the right and left? think in max tallest bars
        total = 0
        left = 0
        right = len(height) - 1
        leftMax = 0
        rightMax = 0
        while (left < right):
            if (height[left] > leftMax):
                leftMax = height[left]
            
            if (height[right] > rightMax):
                rightMax = height[right]
            
            if leftMax < rightMax:
               total += leftMax - height[left]
               left += 1
            else:
                total += rightMax - height[right]
                right -= 1
        return total
