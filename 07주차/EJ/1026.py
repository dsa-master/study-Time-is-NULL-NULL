"""그리디 알고리즘 - 보물문제입니다.
길이가 N인 배열 A와 B가 있음
S = A[0] × B[0] + ... + A[N-1] × B[N-1] 이라는 배열
S의 값을 가장 작게 만들기 위해 A의 값을 재배열(B의 값은 재배열 x)
이 때 S의 최솟값 출력
"""

N = int(input())
Aarr = list(map(int,input().split()))
Barr = list(map(int,input().split()))
# 근데 그냥 든 생각이 출력값은 s의 최촛값만 출력하면 되니까 서로  역 방향으로 sort 해가주고 곱해주면 안되나?-> 이게 맞네 ㅋㅋ

Aarr.sort(reverse=False)
Barr.sort(reverse=True)

S = 0
for i in range(N) :

    S += Aarr[i]*Barr[i]

print(S)