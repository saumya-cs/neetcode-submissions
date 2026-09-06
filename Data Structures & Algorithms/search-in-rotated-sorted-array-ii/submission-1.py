class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        while left <= right:
            #which half is sorted perfectly?
            mid = (left + right) // 2
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[mid] == target:
                return True
            elif nums[mid] >= nums[left]: #left is sorted
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: #right is sorted
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False