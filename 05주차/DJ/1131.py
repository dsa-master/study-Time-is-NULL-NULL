import functools
import typing


@functools.cache
def s(n: int, k: int) -> int:
    acc = 0
    while n > 0:
        acc += (n % 10) ** k
        n //= 10
    return acc


visited = set()
cache: typing.Dict[int, typing.List[int]] = {}

def sequence(n: int, k: int) -> typing.List[int]:
    if n not in cache:
        cache[n] = [n]
        if n in visited:
            visited.clear()
        else:
            visited.add(n)
            cache[n].extend(sequence(s(n, k), k))
    return cache[n]


def main():
    A, B, K = map(int, input().split())
    ans = 0
    for n in range(A, B+1):
        ans += min(n, *sequence(n, K))
    print(ans)


if __name__ == '__main__':
    main()