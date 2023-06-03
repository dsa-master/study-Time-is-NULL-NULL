"""
백준 1003번
피보나치 수열
"""

import sys

t = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(t)]

# 정수 n의 범위 0 <= n <= 40
dp = []
for _ in range(41):
    dp.append([0, 0])

dp[0][0] = 1
dp[1][1] = 1

for i in range(2, 41):
    dp[i][1] = dp[i-1][1] + dp[i-2][1]
    dp[i][0] = dp[i-1][0] + dp[i-2][0]

for number in numbers:
    print(dp[number][0], dp[number][1])
