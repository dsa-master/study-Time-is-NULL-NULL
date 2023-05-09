import sys
import itertools


def main():
    N, K = map(int, sys.stdin.readline().split())
    T = []
    for n in range(N):
        T.append(list(map(int, sys.stdin.readline().split())))

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if T[i][j] > T[i][k] + T[k][j]:
                    T[i][j] = T[i][k] + T[k][j]

    passes = [i for i in range(N) if i != K]
    answer = sys.maxsize
    for routes in itertools.permutations(passes, len(passes)):
        dist = 0
        prev = K
        for next in routes:
            dist += T[prev][next]
            prev = next
        answer = min(answer, dist)

    print(answer)


if __name__ == "__main__":
    main()
