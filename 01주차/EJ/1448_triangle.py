"""
백준 1448: 삼각형 만들기
N개의 빨대 중 3개를 선택했을 때 삼각형 만들 수 있다면 세 변의 길이의 합의 최댓값
입력 : 첫째 줄 N (3<=N<=1000000), 둘째 줄부터 N개의 줄에 빨대의 길이가 한 줄에 하나(빨대의 길이 1000000보다 작거나 같은 자연수)
출력: 삼각형 세 변의 길이의 합의 최대값을 출력 , 출력 불가면 -1

"""
N = int(input())
Nlist = []
# N 입력받기
for i in range(N):
    addN = int(input())
    Nlist.append(addN)

Nlist.sort(reverse=True)   # 내림차순으로 리스트 정렬

# 맨앞 세자리가 삼각형 조건 성립 안되면 한칸 옆으로 이동 -> 나올 때 까지 루프돌리고 더하면 될 듯?

for i in range(len(Nlist)-2) :
    if Nlist[i] < Nlist[i+1] + Nlist[i+2] :
        NSum = Nlist[i] + Nlist[i+1] + Nlist[i+2]
        break
    NSum = -1

print(NSum)
