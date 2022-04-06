class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        queue = deque() # (x, y)
        output = float(-inf)
        for x, y in points:
            while queue and x - queue[0][0] > k:
                queue.popleft()
            if queue:
                output = max(output, queue[0][1] + y + x)
            while queue and y-x > queue[-1][1]:
                queue.pop()
            queue.append((x,y-x))
        return output
