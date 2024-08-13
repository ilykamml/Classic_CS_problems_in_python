from functools import lru_cache


@lru_cache(maxsize=None)
def fib_auto_cache(n: int) -> int:
    if n < 2:
        return n
    return fib_auto_cache(n - 1) + fib_auto_cache(n - 2)


if __name__ == '__main__':
    print(f'5   = {fib_auto_cache(5)}')
    print(f'500 = {fib_auto_cache(500)}')
    print(f'800 = {fib_auto_cache(800)}')
    print(f'1000 = {fib_auto_cache(1000)}')  # I AMM SUPER SPEEED
    print(fib_auto_cache.cache_info())

