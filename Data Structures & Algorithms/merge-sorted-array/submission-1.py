class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        Input: nums1 = [10,20,20,40,0,0], m = 4, nums2 = [1,2], n = 2
        tmp = 10
        nums1 = [1,20,20,40,0,0], nums2 = [10,2]
        """
        
        if n == 0:
            return nums1
        one, two = m-1,n-1
        idx = m + n - 1
        while (idx >= 0):
            if one >= 0:
                val1 = nums1[one]
            else:
                val1 = float('-inf')
            if two >= 0:
                val2 = nums2[two]
            else:
                val2 = float('-inf')
    
            if val1 > val2:
                nums1[idx] = val1
                one -= 1
            else:
                nums1[idx] = val2
                two -= 1
            idx -= 1
       


        