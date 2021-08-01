"""
DFS
"""


def coloring_area(grid):
    
    color = 2
    n = len(grid)
    def neighbors(r, c):
        for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= nr < n and 0 <= nc < n:
                yield nr, nc

    def dfs(r, c, color):
        grid[r][c] = color
        for nr, nc in neighbors(r, c):
            if grid[nr][nc] == 1:
                dfs(nr, nc, color)
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                dfs(r, c, color)
                color += 1
    return grid
