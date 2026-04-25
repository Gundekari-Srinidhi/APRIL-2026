class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = []
        visited = set()

        def goal(state):
            r, c = state
            return (r == 0 or c == 0 or r == len(maze)-1 or c == len(maze[0])-1)

        row, col = entrance
        visited.add((row, col))
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for dr, dc in directions:
            i, j = row + dr, col + dc
            if 0 <= i < len(maze) and 0 <= j < len(maze[0]) and maze[i][j] == ".":
                q.append(((i, j), 1))
                visited.add((i, j))

        while q:
            curr, step = q.pop(0)

            if goal(curr):
                return step  

            row, col = curr

            for dr, dc in directions:
                i, j = row + dr, col + dc
                if (0 <= i < len(maze) and 0 <= j < len(maze[0]) and maze[i][j] == "." and (i, j) not in visited):

                    q.append(((i, j), step + 1))
                    visited.add((i, j))

        return -1