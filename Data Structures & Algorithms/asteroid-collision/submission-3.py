class Solution:
    
    
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # print(f"input list = {asteroids}")
        if not asteroids:
            return asteroids
        stack = []
        #
        for i in range(len(asteroids)): 
            
            alive = True
            while stack and (stack[-1] > 0 and asteroids[i] < 0): #will collide
                leftSize = abs(stack[-1])
                rightSize = abs(asteroids[i])
                if rightSize < leftSize:
                    alive = False
                    break
                elif leftSize < rightSize:
                    stack.pop()
                else: #equal, both explode
                    stack.pop()
                    alive = False
                    break
            if alive:
                stack.append(asteroids[i])
        return stack
            