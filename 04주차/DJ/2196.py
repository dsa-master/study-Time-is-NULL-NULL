from __future__ import annotations

import collections
import sys
import typing


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


def solve(binary: int, numbers: typing.Iterable[int]):
    xor_counter: typing.Dict[int, int] = { num: 0 for num in numbers }

    # 0은 어떤 숫자로도 만들 수 있음 (자기자신과 XOR):
    xor_counter[0] = 1

    ans_num = 0
    ans_sim = simillarity(binary, ans_num)

    queue: typing.Deque[int] = collections.deque(xor_counter.keys())
    while queue:
        x = queue.popleft()
        for y in list(xor_counter):
            z = x ^ y
            if z in xor_counter:
                continue
            xor_counter[z] = xor_counter[x] + xor_counter[y] + 1
            queue.append(z)
            z_sim = simillarity(binary, z)
            if xor_counter[z] > 0 and ans_sim > z_sim or ans_sim == z_sim and z < ans_num:
                ans_num = z
                ans_sim = z_sim
    return '\n'.join([str(xor_counter[ans_num]), bin(ans_num).lstrip('0b')])


def main():
    B, E = map(int, sys.stdin.readline().split())
    X = int(sys.stdin.readline(), base=2)
    Y = map(lambda s: int(s, base=2), [sys.stdin.readline() for _ in range(E)])
    print(solve(X, Y))


if __name__ == '__main__':
    main()