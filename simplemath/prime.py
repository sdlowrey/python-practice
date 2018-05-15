"""A very simple prime number library."""


def is_prime(n: int) -> bool:
    if n < 1:
        return False
    factors = {1, n}
    for i in range(1, n):
        for j in range(1, n):
            if i * j == n:
                factors.update({i, j})
    if len(factors) == 2:
        return True
    return False
