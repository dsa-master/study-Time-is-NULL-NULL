import sys

sys.setrecursionlimit(int(5e6)+32)


def f(n, k):
    if n == 1:
        return 1
    return ((f(n-1, k) + k - 1) % n) + 1


def main():
    N, K = map(int, input().split())
    print(f(N, K))


if __name__ == '__main__':
    main()