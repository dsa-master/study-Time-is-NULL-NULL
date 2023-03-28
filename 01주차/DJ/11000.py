import heapq
import sys
import typing


def solve(lectures: typing.List[typing.Tuple[int, int]]) -> int:
    lectures.sort()
    heap = [] # 강의실 별 수업이 끝나는 시간
    for s, e in lectures:
        if heap and s >= heap[0]:
            # 기존 강의실에 수업을 추가 할 수 있는 경우
            heapq.heappop(heap)
        heapq.heappush(heap, e)
    return len(heap)


def main():
    N = int(sys.stdin.readline())
    lectures: typing.List[typing.Tuple[int, int]] = []
    for _ in range(N):
        lectures.append(tuple(map(int, sys.stdin.readline().split())))
    print(solve(lectures))


if __name__ == "__main__":
    main()