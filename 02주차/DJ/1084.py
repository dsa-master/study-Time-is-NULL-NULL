'''
Author: Hepheir <hepheir@gmail.com>
https://www.acmicpc.net/problem/1084

문제:
    1084번 - 방 번호 2

알고리즘 분류:
    #Greedy #Implementation

풀이:
    각 테스트 케이스마다 O(N^2) 으로 풀이.

    BigInteger 나눗셈 처리가 필요했던 문제로 추정되나,
    python으로 풀이했기에 fractions 모듈을 사용하여 쉽게 처리 함.

    N이 최대 10으로 작은 값이어서 N^2에도 무난한 풀이가 가능하였음.

주요 알고리즘:
    1. 가격 순으로 숫자를 정렬한다. (O(N log N), 과정 2-그리디를 위한 전처리 과정)
    2. 자릿수가 큰 숫자가 가장 큰 숫자이므로, 가장 저렴한 숫자를 최대한 많이 구매한다. (O(1), 그리디)
    3. 만약 0만 구매했다면, 적어도 1개 이상의 다른 숫자로 대체한다.
    4. 가능하다면, 차액을 지불하여 작은 숫자들을 큰 숫자들로 대체한다. O(N^2)
    5. 숫자가 큰 순서대로 높은 자릿수에, 작은 순서대로 낮은 자릿수에 배치하여 정답을 출력한다.
'''

import fractions
import math
import typing


USE_MULTIPLE_TESTCASES = False


def solve(nNumbers: int, numberPrices: typing.List[int], budget: int) -> None:
    numberCounts: typing.List[int] = [0] * nNumbers

    # 1. preprocess (sort by price)
    numberByPrices: typing.List[int] = list(sorted(range(nNumbers), key=lambda num: numberPrices[num] * 11 + -num))

    # 2. buy cheapest
    buyableAmount = math.floor(fractions.Fraction(budget, numberPrices[numberByPrices[0]]))
    numberCounts[numberByPrices[0]] = buyableAmount
    budget -= numberPrices[numberByPrices[0]] * buyableAmount

    # 3. if the cheapest number is zero, try to buy at least one non-zero number
    if numberByPrices[0] == 0 and nNumbers >= 2:
        requiredBudget = numberPrices[numberByPrices[1]] - budget
        amountToSell = math.ceil(fractions.Fraction(requiredBudget, numberPrices[numberByPrices[0]]))
        if numberCounts[numberByPrices[0]] >= amountToSell:
            budget += numberPrices[numberByPrices[0]] * amountToSell
            numberCounts[numberByPrices[0]] -= amountToSell
            budget -= numberPrices[numberByPrices[1]]
            numberCounts[numberByPrices[1]] += 1

    # 4. if possible, replace all the lower numbers with higher numbers :: O(N^2)
    for src in reversed(range(nNumbers)):
        for dst in reversed(range(src+1, nNumbers)):
            priceDiff = numberPrices[dst] - numberPrices[src]
            changeableCount = 0
            if priceDiff <= 0:
                # 큰 숫자를 무료 혹은 돈을 더 받고 바꿀 수 있으면 다 바꾸기
                changeableCount = numberCounts[src]
            else:
                changeableCount = min(numberCounts[src], budget // priceDiff)
            budget += numberPrices[src] * changeableCount
            numberCounts[src] -= changeableCount
            budget -= numberPrices[dst] * changeableCount
            numberCounts[dst] += changeableCount

    # 5. print the result
    nDigits = sum(numberCounts)

    # 5-1. if cannot make a number
    if nDigits == 0:
        print(0)
        return

    # 5-2. in the case that only have zeros
    if numberCounts[0] == nDigits:
        numberCounts[0] = 1
        nDigits = 1

    left = ''
    right = ''
    for number in reversed(range(nNumbers)):
        left = left + str(number) * min(numberCounts[number], 50-len(left))
        if len(left) == 50:
            break
    for number in range(nNumbers):
        right = str(number) * min(numberCounts[number], 50-len(right)) + right
        if len(right) == 50:
            break
    print(nDigits)
    print(left)
    print(right)


def main():
    N = int(input())
    P = list(map(int, input().split()))
    M = int(input())
    solve(N, P, M)


if __name__ == "__main__":
    if USE_MULTIPLE_TESTCASES:
        T = int(input())
        for tc in range(T):
            print(f'\n#{tc+1}')
            main()
    else:
        main()