"""
2023-04-30
RGB 거리
백준 1149번
"""

import sys

n = int(input())
rgb = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 2번째 집부터 시작해서 갱신
for i in range(1, n):
    rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2]) + rgb[i][0] # R
    rgb[i][1] = min(rgb[i-1][0], rgb[i-1][2]) + rgb[i][1] # G
    rgb[i][2] = min(rgb[i-1][0], rgb[i-1][1]) + rgb[i][2] # B

print(min(rgb[n-1]))