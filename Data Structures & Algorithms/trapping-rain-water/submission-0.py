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
            else:
                if leftMax < rightMax:
                    total = total + (rightMax - height[left])
                else:
                    total = total + (leftMax - height[left])
            if (height[right] > rightMax):
                rightMax = height[right]
            else:
                if leftMax < rightMax:
                    total = total + (rightMax - height[right])
                else:
                    total = total + (leftMax - height[right])
            left+=1
            right-=1
        return total
