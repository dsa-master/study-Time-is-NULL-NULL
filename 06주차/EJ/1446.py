"""
D킬로미터의 고속도로 -> 커브가 많다. 지름길 -> 모든 지름길은 일방통행이고 역주행 X
운전해야 하는 거리의 최솟값
첫째 줄 지름길의 개수 N(N<=12),고속도로 길이 D(D<=10000)
다음줄부터 N개 줄에 지름길의 시작 위치, 도착 위치, 지름길의 길이가 주어진다.
모든 위치와 길이는 10000보다 작거나 같은 음이 아닌 정수이다.
지름길의 시작 위치는 도착 위치보다 작다.
"""

# 거리 하나하나를 노드로 보기
# 노드로 보았을때 일단 최소 거리는 for 문을 통해 1로 초기화 (노드 i 에서 다음 노드 i+1까지의 거리는 1)
# 이후 지름길의 정보가 들어오면 graph에 추가
# 만약 지름길의 정보에서 지름길이 끝나는지점이 목표지점 D보다 크면 추가X
import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        #지금 힙큐에서 뺀게 now까지 가는데 최소비용이 아닐수도 있으니 체크
        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))


N , D = map(int,input().split())
graph = [[] for _ in range(D+1)]
distance = [float('inf')] * (D+1)

# 일단 거리 1로 초기화.
for i in range(D):
    graph[i].append((i+1, 1))

# 지름길 있는 경우에 업데이트
for _ in range(N):
    start, end, length = map(int,input().split())
    if end > D:     # 끝나는 지점이 목표지점보다 큰 경우 고려 ㄴㄴ
        continue
    graph[start].append((end,length))

dijkstra(0)
print(distance[D])