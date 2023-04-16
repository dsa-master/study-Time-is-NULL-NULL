from __future__ import annotations

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


def simillarity(x:int , y: int) -> int:
    """숫자의 가까운 정도"""
    return count_bit(x ^ y)


def solve(binary: int, numbers: typing.Tuple[int]):
    xor_counter: typing.List[int] = [0] * NUMBERS

    # 0은 어떤 숫자로도 만들 수 있음 (자기자신과 XOR):
    xor_counter[0] = 1

    queue: typing.Deque[int] = collections.deque(numbers)
    while queue:
        x = queue.popleft()
        for y in numbers:
            z = x ^ y
            if xor_counter[z] != 0:
                continue
            xor_counter[z] = xor_counter[x] + 1
            queue.append(z)

    # O(n)
    ans_num = 0
    ans_sim = simillarity(binary, 0)
    for i in range(NUMBERS):
        if xor_counter[i] < 1:
            continue
        num_sim = simillarity(binary, i)
        if num_sim < ans_sim:
            ans_num = i
            ans_sim = num_sim

    return '\n'.join([str(xor_counter[ans_num]), bin(ans_num).lstrip('0b')])


def main():
    B, E = map(int, sys.stdin.readline().split())
    X = int(sys.stdin.readline(), base=2)
    Y = tuple(map(lambda s: int(s, base=2), [sys.stdin.readline() for _ in range(E)]))
    print(solve(X, Y))


if __name__ == '__main__':
    main()