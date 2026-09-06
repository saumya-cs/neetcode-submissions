class Solution:
    def sameSign(self, one, two) -> bool:
        if one >= 0 and two >= 0:
            return True
        if one < 0 and two < 0:
            return True
        return False
    
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # print(f"input list = {asteroids}")
        if not asteroids:
            return asteroids
        stack = [asteroids.pop()]
        
        for i in range(len(asteroids)-1,-1,-1): #go backwards through array
            # print(f"index = {i}")
            # print(f"stack = [{stack}]")
            right = stack.pop()
            left = asteroids[i]
            # print(f"right = {right}, left = {left}")
            if not self.sameSign(left,right): #going in opposite directions, should collide
                # print("opposite directions")
                if left < 0 and right > 0:
                    stack.append(right)
                    stack.append(left)
                elif abs(right) < abs(left):
                    stack.append(left)
                elif abs(left) < abs(right):
                    stack.append(right)
            else: #shouldn't collide
                stack.append(right)
                stack.append(left)
        answer = []
        while (stack):
            answer.append(stack.pop())
        return answer