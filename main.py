import time
import timeit

import fibonnaci


n = 10000

def main() -> None:
    """The main program."""

    elapsed = timeit.timeit(lambda: 1234 ** 123)
    print(f"Warmup complete in {elapsed:.2f} seconds.")

    fibs = [(fib.fib, fib.__name__.split('.')[-1]) for fib in fibonnaci.modules]

    for fib, name in fibs:
        start_time = time.perf_counter_ns()
        print(f"{name}({n}):".ljust(25) + f"{time.perf_counter_ns() - start_time} ns")
        
    print()
    iterations = int(1e5)
    for fib, name in fibs:
        print(f"{iterations} iterations for {name}({n}):")
        elapsed = timeit.timeit(lambda: fib(n), number=iterations)
        print(f"Elapsed\t\t : {elapsed:.4g} s")

if __name__ == '__main__':
    main()