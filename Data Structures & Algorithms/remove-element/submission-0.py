class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        while (right >= 0 and nums[right] == val):
            right -= 1
        count = 0
        while (left < right):
            if nums[left] == val:
                #swap left and right and move both
                count += 1
                nums[left] = nums[right]
                nums[right] = val
                while (right >= 0 and nums[right] == val):
                    right -= 1
            left += 1
        if left == right:
            if nums[left] == val:
                count += 1
        return len(nums) - count - 1