class MedianFinder:

    def __init__(self):
        self.left_half = [] #max heap
        self.right_half = [] #min heap
        self.total_nums = 0
    def addNum(self, num: int) -> None:
   
        #can assign to correct half and keep even
        placement = "right"
        if not self.left_half:
            placement = "left"
        elif self.left_half and num <= self.left_half[0] * -1: #add to right
            placement = "left"
        
    
        if placement == "left":
            heapq.heappush(self.left_half, -1 * num)
        else:
            heapq.heappush(self.right_half, num)
        
        if len(self.left_half) - len(self.right_half) > 1:
            elem = heapq.heappop(self.left_half)
            heapq.heappush(self.right_half, elem * -1)
        if len(self.right_half) - len(self.left_half) > 1:
            elem = heapq.heappop(self.right_half)
            heapq.heappush(self.left_half, elem * -1)
        self.total_nums += 1
    def findMedian(self) -> float:
        left, right = 0,0
        if self.left_half:
            left = self.left_half[0]
        if self.right_half:
            right = self.right_half[0]
        if self.total_nums % 2 == 0:
            return  (-1 * left + right) / 2
        else:
            if len(self.right_half) > len(self.left_half):
                return right
            else:
                return -1 * left
        