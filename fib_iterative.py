def fib_iterative(n: int) -> int:
    if n == 0: return 0
    last: int = 0
    next_elem: int = 1
    for _ in range(1, n):
        last, next_elem = next_elem, last + next_elem
    return next_elem


if __name__ == '__main__':
    for n in range(1, 101):
        print(f'{n=} \t| {fib_iterative(n)=}')