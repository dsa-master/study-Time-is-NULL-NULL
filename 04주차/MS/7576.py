"""
2023-04-13
토마토
백준 7576번
"""

import sys
from collections import deque

direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
m, n = map(int, sys.stdin.readline().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

q = deque()
result = 0

# 익은 토마토 찾기
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append((i, j))


while q:
    # print(f'{result} DAY, q={q}')
    count = len(q)
    for i in range(count):
        x, y = q.popleft()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
                tomato[nx][ny] = 1
                q.append((nx, ny))

    result += 1

zero = False
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            zero = True

if zero:
    print(-1)
else:
    print(result - 1)


