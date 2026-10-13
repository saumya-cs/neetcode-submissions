class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in range(len(asteroids)):
            end = False
            while not end:
                if not stack:
                    stack.append(asteroids[i])
                    end = True
                elif stack[-1] < 0 and asteroids[i] < 0 or stack[-1] > 0 and asteroids[i] > 0:
                    stack.append(asteroids[i])
                    end = True
                elif (stack[-1] > 0 and asteroids[i] < 0):
                    if abs(stack[-1]) == abs(asteroids[i]):
                        stack.pop()
                        end = True
                    elif abs(stack[-1]) < abs(asteroids[i]):
                        stack.pop()
                    else:
                        end = True
                else:
                    stack.append(asteroids[i])
                    end = True
                    
        return stack
        