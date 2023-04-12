from __future__ import annotations

import collections
import heapq
import sys
import typing


def count_diff(x:int , y: int) -> int:
    """서로 다른 비트의 개수"""
    b = x ^ y
    cnt = 0
    while b > 0:
        if b & 1:
            cnt += 1
        b >>= 1
    return cnt


class Node:
    def __init__(self, number: int, xor_count: int, target: int) -> None:
        self.number = number
        self.xor_count = xor_count
        self.diff = count_diff(target, number)
        self.visited = False

    def __lt__(self, o: Node) -> bool:
        if self.diff != o.diff:
            return self.diff < o.diff
        if self.xor_count != o.xor_count:
            return self.xor_count < o.xor_count
        return self.number < o.number

    def __hash__(self) -> int:
        return self.number

    def __str__(self) -> str:
        return bin(self.number).lstrip('0b')

    def __repr__(self) -> str:
        return self.__str__()

    def do_xor(self, o: Node, target: int) -> Node:
        return Node(self.number ^ o.number, self.xor_count + o.xor_count + 1, target)


def solve(target: int, numbers: typing.List[int]) -> Node:
    pq: typing.List[Node] = []
    _pq: typing.List[Node] = []
    nodes: typing.Dict[int, Node] = {}
    for num in numbers:
        nodes[num] = Node(num, 0, target)
        heapq.heappush(pq, nodes[num])
    while True:
        if not pq:
            if not _pq:
                break
            pq, _pq = _pq, pq
            for x in pq:
                nodes[x.number] = x
        x = heapq.heappop(pq)
        if x.visited:
            continue
        x.visited = True
        for y in tuple(nodes.values()):
            if (x.number ^ y.number) in nodes:
                continue
            heapq.heappush(_pq, x.do_xor(y, target))
    return sorted(nodes.values())[0]


def main():
    B, E = map(int, sys.stdin.readline().split())
    target = int(sys.stdin.readline(), base=2)
    numbers = []
    for i in range(E):
        numbers.append(int(sys.stdin.readline(), base=2))
    node = solve(target, numbers)
    print(node.xor_count)
    print(node)


if __name__ == '__main__':
    main()