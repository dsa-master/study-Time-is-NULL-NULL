step = 0

def dfs_virus (graph, start, visited) :
    global step
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            step += 1
            # print("step :", step)
            dfs_virus(graph, node, visited)


N = int(input())
P = int(input())
cgraph = [[] for i in range(N+1)]

# 컴퓨터 별로 연결된 번호 입력 받기
# 생각해 낸 것 : 쌍에 있는 숫자 중 하나에 해당하는 그래프에 다 넣기
for i in range(P) :
    pair = []
    pair .extend(map(int, input().split()))
    one = pair[0]
    two = pair[1]
    if one not in cgraph[two] :
        cgraph[two].append(one)
    if two not in cgraph[one] :
        cgraph[one].append(two)
        # print(i,"그래프: ",cgraph)

visited=[]
dfs_virus(cgraph,1,visited)
print(step)
