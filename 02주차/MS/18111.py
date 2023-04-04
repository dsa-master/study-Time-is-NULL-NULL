"""
2023-04-02
마인크래프트
백준 18111번
"""
import sys

m, n, b = map(int, sys.stdin.readline().split())

maps = []

min_height = 256
max_height = 0

for _ in range(m):
    temp = list(map(int, sys.stdin.readline().split()))
    min_height = min(min_height, min(temp))
    max_height = max(max_height, max(temp))
    maps.append(temp)

result = []

for k in range(min_height, max_height + 1):
    up = 0  # 설치해야할 블록
    down = 0 # 캐야할 블록

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if k > maps[i][j]:  # 채우는 경우
                up += k - maps[i][j]
            elif k < maps[i][j]:  # 캐는 경우
                down += maps[i][j] - k

    # print(f'[{k}] : up={up} down={down} max={max_height} min={min_height} block={b}')

    if b + down >= up:
        result.append((up + down * 2, k))

result = sorted(result, key=lambda x: (x[0], -x[1]))

print(result[0][0], result[0][1])
