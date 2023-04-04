"""
모니터가 잘 나오는지 테스트하는 프로그램
첫째 줄 s n 입력 : 가로가 s+2 세로 2s+3 n은 모니터에 나와야 하는 수
길이가 s인 '-'와 '|'를 이용해서 출력
"""

# n을 입력받으면, n의 각 자리수를 배열에 넣고 배열을 루프를 돌려서 해당 숫자에 해당하는 이미지?를 올리면 될 것 같음

# 이미지를 그리는 방법 ? 이 중요한 듯
# 숫자 부분에 그림이 들어갈 수 있는 구역이 총 7 군데임 숫자별로 구역에 들어가나 안들어가나 확인하고 이미지를 넣으면 될 것 같다.
# 근데 전혀 모르겠다.ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
"""rows = 2*s+3
cols = s+2
3시간 보고 결국 구글링
"""
import sys
input = sys.stdin.readline

h, v = '-', '|'
s, n = input().split()
s = int(s)


def construct_segment(n):
    lcd = [[' ']*(s+2) for _ in range(2*s + 3)]
    for i in range(1, s+1):
        if n in '02356789':
            lcd[0][i] = h  # a
        if n in '01234789':
            lcd[i][-1] = v  # b
        if n in '013456789':
            lcd[s+1+i][-1] = v  # c
        if n in '0235689':
            lcd[2*s + 2][i] = h  # d
        if n in '0268':
            lcd[s+1+i][0] = v  # e
        if n in '045689':
            lcd[i][0] = v  # f
        if n in '2345689':
            lcd[s+1][i] = h  # g
    return lcd


display = [construct_segment(i) for i in n]

for line in zip(*display):
    for r in line:
        print(''.join(r), end=' ')
    print()

