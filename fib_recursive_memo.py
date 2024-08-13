from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1}  # base cases


def fib_memo(n: int) -> int:
    if n not in memo:
        memo[n] = fib_memo(n - 1) + fib_memo(n - 2)  # memoization
    return memo[n]


if __name__ == '__main__':
    for i in range(0, 1001):
        print(f'{i=} \t| {fib_memo(i)=}')  # I AM SPEED