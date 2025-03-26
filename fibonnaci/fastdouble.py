def fib(n: int) -> int:
    """Compute the nth Fibonacci number using the fast doubling method."""

    def _fib_helper(m):
        if m == 0:
            return (0, 1)
        a, b = _fib_helper(m // 2)
        c = a * (2 * b - a)
        d = a * a + b * b
        if m % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)
    
    return _fib_helper(n)[0]