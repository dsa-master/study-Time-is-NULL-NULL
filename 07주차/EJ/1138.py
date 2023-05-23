"""
구현 - 한줄로 서기 입니당
한줄로 서는  N명의 사람들이 있고 이 사람들은 키가 1~N임( 다 다름)
그리고 각자 왼쪽에 자신보다 왼쪽에 큰사람이 몇명 있었는지 기억함
이 사람들의 전체 배치 정보를 출력하면 됨
"""
N = int(input())
Nlist = list(map(int,input().split()))

# 일단 1의 위치는 바로 알 수 있음 Nlist[0]+1번째
# 또 생각해보니 키 순서대로 배치하면 되겠네 자리를 채운 기준으로 빈 자리가 남아있는 자리에 키 채우면 됨
# 키가 작은 사람부터 result에 넣고 0의 갯수로 자신보다 키 큰 사람이 왼쪽에 몇 명 있는지 파악한다.
result = [0] * N
for i in range(1, N+1):
    t = Nlist[i-1]
    cnt = 0
    for j in range(N):
        if cnt == t and result[j] == 0:
            result[j] = i
            break
        elif result[j] == 0:
            cnt += 1
print(*result) #그냥 *빼고 하니까 틀리네 이거

