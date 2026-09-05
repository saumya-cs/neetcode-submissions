class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #what matters?
            # it can't just be the sum of all bananas
            # can only eat from one pile per hour
            # if h = piles.length, answer is max number in list

            left = 1
            right = max(piles)
            best = right
            while (left <= right):
                middle = (right + left ) // 2
                if self.checkNum(piles, h, middle):
                    right = middle - 1
                    best = middle
                else:
                    left = middle + 1
            return best
            
                
            

    def checkNum(self, piles: List[int], h: int, num: int) -> bool:
       hours = 0
       for pile in piles:
            hours += math.ceil(pile / num)
       return hours <= h

            

        