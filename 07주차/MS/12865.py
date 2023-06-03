"""
2023-05-13
평범한 배낭
백준 12865번
"""

import sys

n, k = map(int, sys.stdin.readline().split())
# i 번째 물건을 고를 때, j 만큼의 여유 공간이 있을 때 최댓값을 담는다.
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
item = [[0, 0]]

for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    item.append([w, v])

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j >= item[i][0]:
            dp[i][j] = max(item[i][1] + dp[i-1][j - item[i][0]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

# n 번째 물건까지 골랐고, k 크기의 여유 공간을 가질 때 최대 값
print(dp[n][k])