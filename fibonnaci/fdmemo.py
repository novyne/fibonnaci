cache = {}

def fib(n):
    if n in cache:
        return cache[n]
    if n == 0:
        return 0
    if n <= 2:
        return 1
    k = n // 2
    a = fib(k)
    b = fib(k + 1)
    if n % 2 == 0:
        res = a * (2 * b - a)
    else:
        res = b * b + a * a
    cache[n] = res
    return res