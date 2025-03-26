from typing import NewType

matrix = NewType('matrix', list[list[int,int],list[int,int]])


M: dict[int, matrix] = {1 : [[1, 1], [1, 0]]} # Dictionary references to get M^n


def matrix_mult(a, b):
    return [
        [a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]],
        [a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]]
    ]


def summative_steps_to_n(n: int) -> list[int]:
    """
    Determine the summative (calculative only) steps required to reach n from 1 using only calculated values.

    Args:
        n (int): The goal n.

    Returns:
        list[int]: The summative steps required.
    """

    known_values: list[int] = [1]
    steps = []
    current = 1

    while current != n:
        # get the highest known value such that current + x doesn't exceed n
        k = 0
        for k in sorted(known_values, reverse=True):
            if k + current < n:
                known_values.append(k + current)
                steps.append(k)
                break

        current += k

    return steps + [1]


def multiply_or_get_M(m: matrix, n: int, mult: int) -> matrix:
    """Multiply the given m such that M[1]^n = m by a given mult or retreive m."""

    if n + mult in M:
        return M[n + mult]
    
    if n not in M.keys() or mult not in M.keys():
        raise ValueError("""N or multiplier not present in M keys.""")
    
    m = matrix_mult(M[n], M[mult])
    M[n + mult] = m
    return m


####################################################################################################


def fib(n: int) -> int:
    """Get the nth fibonnaci number."""

    m = M[1]
    m_index = 1
    steps = summative_steps_to_n(n)

    for step in steps:
        m = multiply_or_get_M(m, m_index, step)
        m_index += step

    return m[0][1]