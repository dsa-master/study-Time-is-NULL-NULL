"""
2023-04-05
적록색약
백준 10026번
"""

import sys
from collections import deque

direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
normal = 0
weakness = 0

def stack_dfs(x, y, rgb):
    stack = deque([(x, y)])
    visited[x][y] = True

    while stack:
        cx, cy = stack.pop()
        print(f'cx={cx} cy={cy}')

        for dx, dy in direction:
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] is False and maps[nx][ny] == rgb:
                    stack.append((nx, ny))
                    visited[nx][ny] = True



n = int(input())
maps = [list(sys.stdin.readline().strip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

# print("normal ---- ")
for i in range(n):
    for j in range(n):
        if visited[i][j] is False:
            stack_dfs(i, j, maps[i][j])
            normal += 1

# 초기화
visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if maps[i][j] == 'R':
            maps[i][j] = 'G'

# print("weakness ---- ")
for i in range(n):
    for j in range(n):
        if visited[i][j] is False:
            stack_dfs(i, j, maps[i][j])
            weakness += 1

print(normal, weakness)

"""
5
RRRGR
RRRRG
RRRRR
RRRRR
RRRRR

5
RRRBB
GGBGR
BBBRR
BBRBG
RRRBG

5
RRRRR
RBBBR
RBGBR
RBBBR
RRRRR
"""
