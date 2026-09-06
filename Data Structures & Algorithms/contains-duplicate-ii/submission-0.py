class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        for windowSize in range(2, k+1):
            left = 0
            right = left + windowSize
            while right < len(nums):
                if nums[left] == nums[right]:
                    return True
                left += 1
                right += 1
        return False
        