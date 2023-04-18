"""
백준 1389 - 케빈베이컨의 6단계 법칙
케빈 베이컨의 수: 한사람이 각각의 사람들과 연결된 단계?들의 합
케빈 베이컨의 수가 가장 적은 사람을 찾기
중복되면 고유 번호가 적은 사람 출력
첫쨰 줄 유저의 수 N 친구 관계의 수 M
둘째 줄 부터 M개의 불에는 친구 관계
"""

# 생각?! 모든 노드까지의 거리의 합이 가장 적은 노드를 찾으면 될 듯!
# 근데 모든 노드까지의 거리의 합을 어떻게 구하지?!

from collections import deque
def bfs(graph, start):
    # num = 지정노드 기준으로 각 노드까지의 거리 시작은 0
    num = [0] * (N+1)
    visited = [start]
    queue = deque()
    queue.append(start)

    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if i not in visited:
                # 거리 기준으로 1씩 더해줌
                num[i] = num[a] + 1
                visited.append(i)
                queue.append(i)
    return sum(num)

N, M = map(int,input().split())
cgraph = [[] for i in range(N+1)]
# 노드들 입력받아 각 그래프에 넣어주기
for i in range(M) :
    pair = []
    pair .extend(map(int, input().split()))
    one = pair[0]
    two = pair[1]
    if one not in cgraph[two] :
        cgraph[two].append(one)
    if two not in cgraph[one] :
        cgraph[one].append(two)

result = []
for i in range(1, N+1):
    result.append(bfs(cgraph, i))

# 해당하는 노드의 index값(최소) 호출
print(result.index(min(result))+1)
