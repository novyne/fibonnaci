def fib(n: int) -> int:
    """Get the nth fibonnaci number."""

    fibx = 0
    fiby = 1

    for _ in range(n):
        fibx, fiby = fiby, fibx + fiby

    return fibx