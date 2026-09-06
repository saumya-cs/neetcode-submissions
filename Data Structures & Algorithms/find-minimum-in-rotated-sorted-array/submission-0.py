class Solution:
    def findMin(self, nums: List[int]) -> int:
        #binary search
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2

        while (left < right):
            mid = (left + right) // 2
            #l and mid in same segment
            if(nums[mid] - nums[left] == mid-left):
                left = mid + 1
            #mid and r in same segment
            if(nums[right] - nums[mid] == right-mid):
                right = mid
          
        return nums[left]
        