class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        nums = [1,2,3,4,5,6,7,8], k = 4
        [8,1,2,3,4,5,6,7]
        [7,8,1,2,3,4,5,6]
        [6,7,8,1,2,3,4,5]
        [5,6,7,8,1,2,3,4]

        input array is not necessarily sorted


        """

        def reverseArray(nums, start,end):
            while end >= 0 and start < len(nums) and start < end:
                tmp = nums[start]
                nums[start] = nums[end]
                nums[end] = tmp
                start += 1
                end -= 1
    
        reverseArray(nums,0,len(nums)-1)
        reverseArray(nums,0,k-1)
        reverseArray(nums,k,len(nums) - 1)
        