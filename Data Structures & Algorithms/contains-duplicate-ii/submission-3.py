class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        left = 0
        right = 1
        window = set()
        window.add(nums[left])
        
        while (right < len(nums)):

            if nums[right] in window:
                return True
            
            if right < len(nums):
                window.add(nums[right])
            right += 1
            if right - left > k:
                window.remove(nums[left])
                left += 1
        return False
        