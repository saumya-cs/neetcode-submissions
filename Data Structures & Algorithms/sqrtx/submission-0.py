class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            print(mid)
            guess = mid * mid
            if guess == x:
                return mid
            elif guess > x:
                right = mid - 1
            else:
                left = mid + 1
        return right

        