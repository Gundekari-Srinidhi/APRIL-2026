class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[0])
        n = len(points)
        i = 0
        count = 0

        while i < n:
            val1 = points[i]
            end = val1[1]   

            while i < n-1 and end >= points[i+1][0]:
                end = min(end, points[i+1][1])   
                i += 1
            count += 1
            i += 1
        return count


        