import time
import timeit
import os
from typing import List, Tuple

from matplotlib import pyplot

import fibonnaci

max_fib = int(1e4)
repeat_tests = 1
time_until_ns = 2e9

graphs_dir = "graphs"

def remove_anomalies(data: List[int]) -> List[int]:
    '''Remove anomalies from data using the IQR method.'''
    if len(data) < 4:
        return data
    sorted_data = sorted(data)
    q1 = sorted_data[len(sorted_data) // 4]
    q3 = sorted_data[(len(sorted_data) * 3) // 4]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    filtered = [x for x in data if lower_bound <= x <= upper_bound]
    return filtered

def measure_times(method) -> List[int]:
    times = []
    for n in range(1, max_fib + 1):
        start_time = time.perf_counter_ns()
        for _ in range(repeat_tests):
            method(n)
        elapsed = time.perf_counter_ns() - start_time
        times.append(elapsed / repeat_tests)
    return times

def time_until(method) -> List[int]:
    times = []
    total_start = time.perf_counter_ns()
    cumulative_time = 0

    n = 0
    while True:
        n += 1

        start_time = time.perf_counter_ns()
        for _ in range(repeat_tests):
            method(n)
        elapsed = time.perf_counter_ns() - start_time
        avg_time = elapsed / repeat_tests
        cumulative_time += avg_time
        times.append(cumulative_time)
        total_elapsed = time.perf_counter_ns() - total_start
        if total_elapsed >= time_until_ns * repeat_tests:
            print(f"Time up after f({n}).")
            break
    return times

def plot_single_graph(x: List[int], y: List[int], name: str) -> None:
    os.makedirs(graphs_dir, exist_ok=True)
    pyplot.figure()
    pyplot.plot(x, y, label=name)
    pyplot.xlabel("n")
    pyplot.ylabel("Time (ns)")
    pyplot.title(f"Fibonacci Method Performance: {name} (Anomalies Removed)")
    pyplot.legend()
    filename = os.path.join(graphs_dir, f"fib_performance_{name}.png")
    pyplot.savefig(filename)
    pyplot.close()
    print(f"Saved individual plot: {filename}")

def plot_combined_graph(data: List[Tuple[str, List[int]]]) -> None:
    os.makedirs(graphs_dir, exist_ok=True)
    pyplot.figure()
    for name, times in data:
        pyplot.plot(range(1, len(times) + 1), times, label=name)
    pyplot.xlabel("n")
    pyplot.ylabel("Time (ns)")
    pyplot.title("Fibonacci Method Performance (Anomalies Removed) - Combined")
    pyplot.legend()
    filename = os.path.join(graphs_dir, "fib_performance_combined.png")
    pyplot.savefig(filename)
    pyplot.close()
    print(f"Saved combined plot: {filename}")

def main() -> None:

    # alg = measure_times
    alg = time_until

    elapsed = timeit.timeit(lambda: 1234 ** 123)
    print(f"Warmup complete in {elapsed:.2f} seconds.")

    fibs = [(fib.fib, fib.__name__.split('.')[-1]) for fib in fibonnaci.modules]

    combined_data = []

    for method, name in fibs:
        times = alg(method)
        if alg == measure_times:
            times = remove_anomalies(times)
        plot_single_graph(range(1, len(times) + 1), times, name)
        combined_data.append((name, times))

    plot_combined_graph(combined_data)


if __name__ == '__main__':
    main()
