def main():
    N, K = map(int, input().split())

    ans = 1
    for n in range(1, N+1):
        ans = ((ans + K-1) % n) + 1

    print(ans)


if __name__ == '__main__':
    main()