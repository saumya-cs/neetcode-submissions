class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #what matters?
            # it can't just be the sum of all bananas
            # can only eat from one pile per hour
            # if h = piles.length, answer is max number in list

            left = 1
            right = max(piles)
            best = max(piles)
            while (left < right):
                middle = (right - left ) // 2
                if self.checkNum(piles, h, middle):
                    right = middle
                    best = middle
                else:
                    left = middle
            return best
            
                
            

    def checkNum(piles: List[int], h: int, num: int) -> bool:
        hours = 0
        for i in range(len(piles)):
            if piles[i] <= num:
                hours += 1
            else:
                balance = piles[i]
                while (balance > 0):
                    balance = balance - num
                    hours += 1
        if (hours <= h):
            return True
        else:
            return False

            

        