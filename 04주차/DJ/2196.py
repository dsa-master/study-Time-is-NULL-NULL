import collections
import sys
import typing


NUMBERS = 65536


def count_bit(x: int) -> int:
    cnt = 0
    while x > 0:
        if x & 1:
            cnt += 1
        x >>= 1
    return cnt


def distance(x:int , y: int) -> int:
    return count_bit(x ^ y)


def solve(ndigits:int, binary: int, numbers: typing.Tuple[int]):
    xor_counter: typing.List[int] = [0] * (NUMBERS)
    queue: typing.Deque[int] = collections.deque()

    for x in numbers:
        for y in numbers:
            xor_counter[x^y] = 1
            queue.append(x^y)

    while queue:
        x = queue.popleft()
        for y in numbers:
            z = x ^ y
            if xor_counter[z] == 0:
                xor_counter[z] = xor_counter[x] + 1
                queue.append(z)

    # O(n)
    ans_num = 0
    ans_dist = distance(binary, 0)
    for i in range(NUMBERS):
        if xor_counter[i] < 1:
            continue
        num_dist = distance(binary, i)
        if num_dist < ans_dist:
            ans_num = i
            ans_dist = num_dist

    return '\n'.join([
        str(xor_counter[ans_num]),
        bin(ans_num).lstrip('0b').zfill(ndigits)
    ])


def main():
    B, E = map(int, sys.stdin.readline().split())
    X = int(sys.stdin.readline(), base=2)
    Y = tuple(map(lambda s: int(s, base=2), [sys.stdin.readline() for _ in range(E)]))
    print(solve(B, X, Y))


if __name__ == '__main__':
    main()