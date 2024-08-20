import sys
from typing import Generator


def fib_gen(n: int) -> Generator[int, None, None]:
    yield 0  # special case
    if n > 0: yield 1  # special case
    last: int = 0  # base value fib(0)
    next: int = 1  # base value fib(1)
    for _ in range(1, n):
        last, next = next, last + next
        yield next


if __name__ == '__main__':
    generated = fib_gen(500)
    for i, fnum in enumerate(generated):
        print(i, fnum)