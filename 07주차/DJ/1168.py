import typing


ALIVE = 1
DEAD = 0


class SegmentTree:
    def __init__(self, arr: typing.List[int]) -> None:
        n = len(arr)
        self.st = [0] * (4*n)
        self.n = n
        for i in range(n):
            self.update(i, arr[i])
        pass

    def shift_up(self, si: int):
        parent = si >> 1
        while parent > 0:
            lchild = parent << 1
            rchild = lchild + 1
            self.st[parent] = self.st[lchild] + self.st[rchild]
            parent = parent >> 1

    def update(self, index: int, value: int):
        es = 0
        ee = self.n-1
        si = 1
        while es < ee:
            mid = (es+ee)//2
            if mid >= index:
                ee = mid
                si = si * 2
            else:
                es = mid+1
                si = si * 2 + 1
        self.st[si] = value
        self.shift_up(si)

    def query_util(self, si, es, ee, value):
        if es == ee:
            return es
        mid = (es + ee) // 2
        lchild = si << 1
        rchild = lchild+1
        if (value <= self.st[lchild]):
            return self.query_util(lchild, es, mid, value)
        else:
            return self.query_util(rchild, mid+1, ee, value-self.st[lchild])

    def query(self, value: int) -> int:
        return self.query_util(1, 1, self.n, value)

    def sum(self) -> int:
        return self.st[1]


def main():
    N, K = map(int, input().split())

    st = SegmentTree([DEAD]+[ALIVE]*N)
    nth = 1

    print("<", end='')
    for n in range(N, 0, -1):
        nth = (nth+K-1) % n
        if nth == 0:
            nth = n

        next = st.query(nth)
        st.update(next, DEAD)

        print(nth, end='')
        if n > 1:
            print(', ', end='')
    print(">")


if __name__ == '__main__':
    main()