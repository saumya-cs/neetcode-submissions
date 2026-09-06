class Solution:
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
    """
    [left ... i]      < pivot
    [i+1 ... j-1]     >= pivot
    [j ... right-1]   unexplored
    [right]           pivot
    """
    def partition(self, nums, left, right):
        pivot = nums[right]
        i = left - 1
        for j in range(left, right):
            if nums[j] < pivot:
                i += 1
                self.swap(nums,i, j)
        nums[i+1], nums[right] = nums[right], nums[i+1]
        return i + 1
    def quickSort(self, nums, left, right):
        if left >= right:
            return
        final_pivot = self.partition(nums, left, right)
        self.quickSort(nums, left, final_pivot-1)
        self.quickSort(nums, final_pivot + 1, right)
    def sortArray(self, nums: List[int]) -> List[int]:
        #quick sort
        self.quickSort(nums, 0, len(nums)-1)
        return nums
    
        