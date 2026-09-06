class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif mid == len(nums)-1 and nums[mid] < target:
                return mid + 1
            elif mid < len(nums) - 1 and nums[mid] < target and nums[mid+1] > target:
                return mid
            elif mid > 0 and nums[mid] > target and nums[mid-1] < target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        