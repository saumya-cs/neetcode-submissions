class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #input is sorted
        #hint: Given two adjacent windows of size k, can you tell which direction 
        #to move using only information at their boundaries? 0 1 2 3 4 5 

        left = 0
        right = len(arr) - k

        while (left < right):
            mid = (left + right) // 2
            #compare first elem of window starting at mid with last elem of window starting at mid + 1
            first = arr[mid]
            last = arr[mid+k]
            if abs(x - first) <= abs(x - last):
                right = mid
            else:
                left = mid + 1
        return arr[left:left+k]