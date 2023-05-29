"""
가장 긴 증가하는 부분 수열 구하기
첫째 줄에 가장 긴 증가하는 부분 수열의 길이 입력
"""

# DP 문제라는데 너무 어려워요 ㅜㅜㅜㅜㅜㅜ
N = int(input())
arrList = list(map(int,input().split()))

# 결국 참고함
result = [1]*N # DP 배열
for i in range(1,N):
    for j in range(i): # 한 바퀴 쭉 돌면서 증가 할 때 마다 카운트해서 저장
        if arrList[j] < arrList[i]: # arr 배열
            result[i] = max(result[i],result[j]+1) # 증가한다면 카운트

print(max(result))

# 근데 풀이보면 쉽다잉