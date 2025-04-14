class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if -asteroid > stack[-1]:
                    stack.pop()
                    continue
                elif -asteroid == stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        return stack