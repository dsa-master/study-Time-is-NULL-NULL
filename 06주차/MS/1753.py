"""
2023-05-09
최단경로
백준 1753번
"""

import sys
import heapq
INF = int(1e9)

# 정점의 개수, 간선의 개수
v, e = map(int, sys.stdin.readline().split())

# 시작 정점의 번호
start = int(input())

graph = [[] for i in range(v + 1)]

# 최단 거리 테이블
distance = [INF] * (v + 1)

for _ in range(e):
    s, e, w = map(int, sys.stdin.readline().split())
    graph[s].append((e, w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 힙에서 최단 거리 노드 꺼내기
        dist, now = heapq.heappop(q)

        # 처리되었으면 무시
        if distance[now] < dist:
            continue

        for dest, weight in graph[now]:
            cost = dist + weight
            if cost < distance[dest]:
                distance[dest] = cost
                heapq.heappush(q, (cost, dest))

dijkstra(start)

for i in distance[1:]:
    if i == INF:
        print('INF')
    else:
        print(i)