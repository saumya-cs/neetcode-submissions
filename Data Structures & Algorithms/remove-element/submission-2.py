class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # left = 0
        # right = len(nums)
        
        
        # while (left < right):
        #     if nums[left] == val:
        #         #swap left and right and move both
        #         nums[left] = nums[right-1]
        #         right -= 1
        #     else:
        #         left += 1
        
        # return right
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k