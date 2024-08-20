def fib1(n: int) -> int:
    if n < 2:  # base case
        return n
    return fib1(n-1) + fib1(n-2)  # recursive case


if __name__ == '__main__':
    for n in range(0, 11):
        print(f'{n=} \t|\t{fib1(n)=}')