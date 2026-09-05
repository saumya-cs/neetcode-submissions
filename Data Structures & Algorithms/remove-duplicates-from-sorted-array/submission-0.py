class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nextUnique = 1
        idx = 1
        while idx < len(nums):
            if nums[idx-1] == nums[idx]:
                idx += 1
            else:
                nums[nextUnique] = nums[idx]
                nextUnique += 1
                idx += 1
        return nextUnique