class Solution:
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checkNum(num):
            count = 0
            for pile in piles:
                count += (pile // num)
                if pile % num != 0:
                    count += 1

            return count
        piles.sort() #sorted ascendingly
        minSpeed = float('inf')
        left = 1
        right = max(piles)

        while (left <= right):
            mid = (left + right) // 2
            potential_k = checkNum(mid)
            if potential_k > h:
                left = mid + 1
            else:
                right = mid - 1
                minSpeed = min(minSpeed, mid)

        return minSpeed

        #5 6 4 2 3
        

        