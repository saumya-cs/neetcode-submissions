class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        left = 0
        right = 1
        while (right < len(nums)):
            if nums[left] == nums[right]:
                return True
            right += 1
            if right - left > k:
                left += 1
        return False
        