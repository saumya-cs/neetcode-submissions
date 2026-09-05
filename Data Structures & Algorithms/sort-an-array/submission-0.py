class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #merge sort
        def merge(arr, L, M, R):
            left = arr[L:M+1]
            right = arr[M+1:R+1]
            original_idx = L
            left_idx,right_idx = 0,0

            while left_idx < len(left) and right_idx < len(right):
                left_item = left[left_idx]
                right_item = right[right_idx]
                if  left_item < right_item:
                    arr[original_idx] = left_item
                    original_idx += 1
                    left_idx += 1
                else:
                    arr[original_idx] = right_item
                    original_idx += 1
                    right_idx += 1
            while left_idx < len(left):
                arr[original_idx] = left[left_idx]
                left_idx += 1
                original_idx += 1
            while right_idx < len(right):
                arr[original_idx] = right[right_idx]
                right_idx += 1
                original_idx += 1
        def mergeSort(arr, L, R):
            if L >= R:
                return
            m = (L + R) // 2
            mergeSort(arr, L, m)
            mergeSort(arr, m + 1, R)
            merge(arr, L, m, R)
        mergeSort(nums, 0, len(nums)-1)
        return nums
