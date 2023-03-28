"""
2023-03-26
설탕 배달
백준 2839번
"""

n = int(input())

sugar = [-1] * 5001

for kg in [3, 5]:
    for index in range(3, n + 1):
        if index % kg == 0:
            sugar[index] = index // kg
        elif sugar[index] != -1 and index + kg <= 5000:
            # 4995부터 Index Error
            sugar[index + kg] = sugar[index] + 1

print(sugar[n])