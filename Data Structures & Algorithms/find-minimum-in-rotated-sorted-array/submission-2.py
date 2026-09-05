class Solution:
    def findMin(self, nums: List[int]) -> int:
        #min element is when both surrounding elems are greater than it or edge on one side
        #sorted so what are my conditions
        

        left = 0
        right = len(nums) - 1

        while left != right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

        