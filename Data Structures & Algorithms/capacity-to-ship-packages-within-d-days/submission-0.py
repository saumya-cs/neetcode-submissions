class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def checkNum(capacity):
            weights_idx = 0
            days = 1
            curr_cap = capacity
            while (weights_idx < len(weights)):
                if weights[weights_idx] > capacity:
                    return float('inf')
                if weights[weights_idx] > curr_cap:
                    days += 1
                    curr_cap = capacity
                else:
                    curr_cap -= weights[weights_idx]
                    weights_idx += 1
            return days
        
       
        minCapacity = float('inf')
        left = 1
        right = sum(weights)

        while (left <= right):
            mid = (left + right) // 2
            potential_days = checkNum(mid)
            if potential_days <= days:
               right = mid - 1
               minCapacity = min(minCapacity, mid)
            else:
                left = mid + 1

        return minCapacity

        #5 6 4 2 3
        

        